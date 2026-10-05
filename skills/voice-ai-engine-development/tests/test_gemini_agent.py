"""
Tests for skills/voice-ai-engine-development/examples/gemini_agent_example.py
"""

import asyncio
import sys
import unittest
from pathlib import Path
from unittest.mock import AsyncMock, patch

# Add examples directory to sys.path to import gemini_agent_example
examples_dir = Path(__file__).parent.parent / "examples"
if str(examples_dir) not in sys.path:
    sys.path.insert(0, str(examples_dir))

from gemini_agent_example import GeminiAgent, GeneratedResponse, Message


class TestGeminiAgent(unittest.IsolatedAsyncioTestCase):
    def setUp(self):
        self.config = {
            "prompt": "You are a helpful AI assistant.",
            "llmProvider": "gemini"
        }
        self.agent = GeminiAgent(self.config)

    async def test_generate_response_happy_path(self):
        """Test successful response generation and streaming buffer."""
        responses = []
        async for resp in self.agent.generate_response("Hello"):
            responses.append(resp)

        self.assertEqual(len(responses), 1)
        self.assertIsInstance(responses[0], GeneratedResponse)
        self.assertTrue(responses[0].is_interruptible)
        self.assertIn("Hello", responses[0].message)

        history = self.agent.get_conversation_history()
        self.assertEqual(len(history), 2)
        self.assertEqual(history[0].role, "user")
        self.assertEqual(history[0].content, "Hello")
        self.assertEqual(history[1].role, "assistant")

    async def test_generate_response_error_path(self):
        """Test error handling when streaming fails during generation."""
        async def mock_failing_stream(user_input):
            raise RuntimeError("Gemini API connection error")
            yield "never reached"

        self.agent._simulate_gemini_stream = mock_failing_stream

        responses = []
        async for resp in self.agent.generate_response("Trigger Error"):
            responses.append(resp)

        self.assertEqual(len(responses), 1)
        expected_error_msg = "I apologize, but I encountered an error. Could you please try again?"
        self.assertEqual(responses[0].message, expected_error_msg)

        history = self.agent.get_conversation_history()
        self.assertEqual(len(history), 2)
        self.assertEqual(history[0].role, "user")
        self.assertEqual(history[0].content, "Trigger Error")
        self.assertEqual(history[1].role, "assistant")
        self.assertEqual(history[1].content, expected_error_msg)

    def test_build_gemini_contents(self):
        """Test building Gemini contents with system prompt and history."""
        self.agent.conversation_history = [
            Message(role="user", content="Hi"),
            Message(role="assistant", content="Hello!")
        ]
        contents = self.agent._build_gemini_contents()

        # System prompt (user + model response) + 2 history messages = 4 items
        self.assertEqual(len(contents), 4)
        self.assertEqual(contents[0]["role"], "user")
        self.assertIn("You are a helpful AI assistant.", contents[0]["parts"][0]["text"])
        self.assertEqual(contents[1]["role"], "model")
        self.assertEqual(contents[2]["role"], "user")
        self.assertEqual(contents[2]["parts"][0]["text"], "Hi")
        self.assertEqual(contents[3]["role"], "model")
        self.assertEqual(contents[3]["parts"][0]["text"], "Hello!")

    def test_update_last_bot_message_on_cut_off(self):
        """Test updating last bot message when interrupted/cut off."""
        self.agent.conversation_history = [
            Message(role="user", content="Tell me a long story"),
            Message(role="assistant", content="Once upon a time in a faraway land...")
        ]
        self.agent.update_last_bot_message_on_cut_off("Once upon a time")

        history = self.agent.get_conversation_history()
        self.assertEqual(history[-1].content, "Once upon a time")

    async def test_cancel_current_task(self):
        """Test cancelling the current running generation task."""
        async def dummy_task():
            await asyncio.sleep(10)

        task = asyncio.create_task(dummy_task())
        self.agent.current_task = task
        self.agent.cancel_current_task()

        # Allow loop to process cancellation
        try:
            await task
        except asyncio.CancelledError:
            pass

        self.assertTrue(task.cancelled())

    def test_get_and_clear_conversation_history(self):
        """Test retrieving and clearing conversation history."""
        self.agent.conversation_history = [Message(role="user", content="Test")]
        history_copy = self.agent.get_conversation_history()
        self.assertEqual(len(history_copy), 1)

        # Ensure history copy is isolated
        history_copy.append(Message(role="assistant", content="Extra"))
        self.assertEqual(len(self.agent.get_conversation_history()), 1)

        self.agent.clear_conversation_history()
        self.assertEqual(len(self.agent.get_conversation_history()), 0)


if __name__ == "__main__":
    unittest.main()
