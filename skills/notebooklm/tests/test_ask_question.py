import os
import sys
import unittest
from unittest.mock import MagicMock, patch

# Ensure patchright module exists in sys.modules before ask_question import
if "patchright" not in sys.modules:
    mock_patchright = MagicMock()
    sys.modules["patchright"] = mock_patchright
    sys.modules["patchright.sync_api"] = mock_patchright.sync_api

# Ensure scripts directory is in sys.path
SCRIPTS_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "scripts"))
if SCRIPTS_DIR not in sys.path:
    sys.path.insert(0, SCRIPTS_DIR)

from ask_question import ask_notebooklm, FOLLOW_UP_REMINDER


class TestAskNotebookLM(unittest.TestCase):
    @patch("ask_question.AuthManager")
    def test_ask_notebooklm_unauthenticated(self, mock_auth_cls):
        """Test ask_notebooklm returns None when AuthManager indicates not authenticated."""
        mock_auth_instance = MagicMock()
        mock_auth_instance.is_authenticated.return_value = False
        mock_auth_cls.return_value = mock_auth_instance

        result = ask_notebooklm("What is AI?", "https://notebooklm.google.com/notebook/123")
        self.assertIsNone(result)

    @patch("ask_question.StealthUtils")
    @patch("ask_question.BrowserFactory")
    @patch("ask_question.sync_playwright")
    @patch("ask_question.AuthManager")
    def test_ask_notebooklm_query_input_not_found(
        self, mock_auth_cls, mock_playwright_fn, mock_browser_factory, mock_stealth
    ):
        """Test ask_notebooklm returns None if query input element is not found."""
        mock_auth_cls.return_value.is_authenticated.return_value = True

        mock_playwright = MagicMock()
        mock_playwright_fn.return_value.start.return_value = mock_playwright

        mock_context = MagicMock()
        mock_browser_factory.launch_persistent_context.return_value = mock_context

        mock_page = MagicMock()
        mock_context.new_page.return_value = mock_page

        # Simulate wait_for_selector raising an exception / returning None for all selectors
        mock_page.wait_for_selector.side_effect = Exception("Element not found")

        result = ask_notebooklm("What is AI?", "https://notebooklm.google.com/notebook/123")

        self.assertIsNone(result)
        mock_context.close.assert_called_once()
        mock_playwright.stop.assert_called_once()

    @patch("ask_question.time")
    @patch("ask_question.StealthUtils")
    @patch("ask_question.BrowserFactory")
    @patch("ask_question.sync_playwright")
    @patch("ask_question.AuthManager")
    def test_ask_notebooklm_success(
        self, mock_auth_cls, mock_playwright_fn, mock_browser_factory, mock_stealth, mock_time
    ):
        """Test successful question asking and answer retrieval with stability check."""
        mock_auth_cls.return_value.is_authenticated.return_value = True

        mock_playwright = MagicMock()
        mock_playwright_fn.return_value.start.return_value = mock_playwright

        mock_context = MagicMock()
        mock_browser_factory.launch_persistent_context.return_value = mock_context

        mock_page = MagicMock()
        mock_context.new_page.return_value = mock_page

        mock_query_element = MagicMock()
        mock_page.wait_for_selector.return_value = mock_query_element

        # Mock query_selector for thinking element to return None (not thinking)
        mock_page.query_selector.return_value = None

        # Mock query_selector_all for response elements
        mock_response_element = MagicMock()
        mock_response_element.inner_text.return_value = "This is the answer."
        mock_page.query_selector_all.return_value = [mock_response_element]

        # Time mock: return advancing timestamp to avoid infinite loop
        # deadline = time.time() + 120
        # loop condition: time.time() < deadline
        time_values = [100.0, 101.0, 102.0, 103.0, 104.0, 105.0]
        mock_time.time.side_effect = time_values

        result = ask_notebooklm("What is AI?", "https://notebooklm.google.com/notebook/123")

        self.assertEqual(result, "This is the answer." + FOLLOW_UP_REMINDER)
        mock_stealth.human_type.assert_called_once()
        mock_page.keyboard.press.assert_called_with("Enter")
        mock_context.close.assert_called_once()
        mock_playwright.stop.assert_called_once()

    @patch("ask_question.time")
    @patch("ask_question.StealthUtils")
    @patch("ask_question.BrowserFactory")
    @patch("ask_question.sync_playwright")
    @patch("ask_question.AuthManager")
    def test_ask_notebooklm_handles_thinking_element(
        self, mock_auth_cls, mock_playwright_fn, mock_browser_factory, mock_stealth, mock_time
    ):
        """Test that ask_notebooklm waits while thinking element is visible."""
        mock_auth_cls.return_value.is_authenticated.return_value = True

        mock_playwright = MagicMock()
        mock_playwright_fn.return_value.start.return_value = mock_playwright

        mock_context = MagicMock()
        mock_browser_factory.launch_persistent_context.return_value = mock_context

        mock_page = MagicMock()
        mock_context.new_page.return_value = mock_page

        mock_query_element = MagicMock()
        mock_page.wait_for_selector.return_value = mock_query_element

        # Thinking element is visible on first loop iteration, then None on subsequent iterations
        thinking_elem = MagicMock()
        thinking_elem.is_visible.return_value = True

        mock_page.query_selector.side_effect = [thinking_elem, None, None, None, None, None]

        # Response element available after thinking finishes
        mock_response_element = MagicMock()
        mock_response_element.inner_text.return_value = "Final answer text."
        mock_page.query_selector_all.return_value = [mock_response_element]

        time_values = [100.0, 101.0, 102.0, 103.0, 104.0, 105.0, 106.0, 107.0]
        mock_time.time.side_effect = time_values

        result = ask_notebooklm("What is AI?", "https://notebooklm.google.com/notebook/123")

        self.assertEqual(result, "Final answer text." + FOLLOW_UP_REMINDER)

    @patch("ask_question.time")
    @patch("ask_question.StealthUtils")
    @patch("ask_question.BrowserFactory")
    @patch("ask_question.sync_playwright")
    @patch("ask_question.AuthManager")
    def test_ask_notebooklm_timeout_waiting_for_answer(
        self, mock_auth_cls, mock_playwright_fn, mock_browser_factory, mock_stealth, mock_time
    ):
        """Test that ask_notebooklm returns None when deadline is exceeded without stable answer."""
        mock_auth_cls.return_value.is_authenticated.return_value = True

        mock_playwright = MagicMock()
        mock_playwright_fn.return_value.start.return_value = mock_playwright

        mock_context = MagicMock()
        mock_browser_factory.launch_persistent_context.return_value = mock_context

        mock_page = MagicMock()
        mock_context.new_page.return_value = mock_page

        mock_query_element = MagicMock()
        mock_page.wait_for_selector.return_value = mock_query_element

        mock_page.query_selector.return_value = None
        mock_page.query_selector_all.return_value = []

        # Time starts at 100, deadline set to 100 + 120 = 220
        # Next loop iteration returns 230 > 220
        mock_time.time.side_effect = [100.0, 230.0]

        result = ask_notebooklm("What is AI?", "https://notebooklm.google.com/notebook/123")

        self.assertIsNone(result)

    @patch("ask_question.BrowserFactory")
    @patch("ask_question.sync_playwright")
    @patch("ask_question.AuthManager")
    def test_ask_notebooklm_exception_handling(
        self, mock_auth_cls, mock_playwright_fn, mock_browser_factory
    ):
        """Test that exceptions during browser interaction are caught and context is closed."""
        mock_auth_cls.return_value.is_authenticated.return_value = True

        mock_playwright = MagicMock()
        mock_playwright_fn.return_value.start.return_value = mock_playwright

        mock_context = MagicMock()
        mock_browser_factory.launch_persistent_context.return_value = mock_context

        mock_page = MagicMock()
        mock_context.new_page.return_value = mock_page

        mock_page.goto.side_effect = RuntimeError("Browser crash")

        result = ask_notebooklm("What is AI?", "https://notebooklm.google.com/notebook/123")

        self.assertIsNone(result)
        mock_context.close.assert_called_once()
        mock_playwright.stop.assert_called_once()


if __name__ == "__main__":
    unittest.main()
