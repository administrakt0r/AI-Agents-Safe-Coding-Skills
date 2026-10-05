import io
import os
import sys
import unittest
from unittest.mock import MagicMock, patch

# Ensure templates directory is in sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../templates")))

import multi_provider_factory_template as mpf


class TestExampleUsage(unittest.TestCase):
    """Unit tests for the example_usage function"""

    def test_example_usage_not_implemented_error(self):
        """Verify example_usage handles NotImplementedError as designed in template"""
        captured_output = io.StringIO()
        with patch("sys.stdout", captured_output):
            mpf.example_usage()
        output = captured_output.getvalue()
        self.assertIn("⚠️ Not implemented:", output)

    def test_example_usage_success(self):
        """Verify example_usage output when all components are successfully created"""
        captured_output = io.StringIO()
        mock_factory = MagicMock()
        mock_factory.create_transcriber.return_value = MagicMock()
        mock_factory.create_agent.return_value = MagicMock()
        mock_factory.create_synthesizer.return_value = MagicMock()

        with patch("multi_provider_factory_template.VoiceComponentFactory", return_value=mock_factory):
            with patch("sys.stdout", captured_output):
                mpf.example_usage()

        output = captured_output.getvalue()
        self.assertIn("✅ All components created successfully!", output)

    def test_example_usage_value_error(self):
        """Verify example_usage handles ValueError for invalid configuration"""
        captured_output = io.StringIO()
        mock_factory = MagicMock()
        mock_factory.create_transcriber.side_effect = ValueError("Invalid provider test")

        with patch("multi_provider_factory_template.VoiceComponentFactory", return_value=mock_factory):
            with patch("sys.stdout", captured_output):
                mpf.example_usage()

        output = captured_output.getvalue()
        self.assertIn("❌ Configuration error: Invalid provider test", output)


class TestVoiceComponentFactory(unittest.TestCase):
    """Unit tests for VoiceComponentFactory class"""

    def test_create_transcriber_valid_providers(self):
        """Test creating transcribers for supported providers"""
        providers = ["deepgram", "assemblyai", "azure", "google"]
        for provider in providers:
            config = {"transcriberProvider": provider}
            method_name = f"_create_{provider}_transcriber"

            with patch.object(mpf.VoiceComponentFactory, method_name, return_value=f"mock_{provider}") as mock_method:
                factory = mpf.VoiceComponentFactory()
                result = factory.create_transcriber(config)
                self.assertEqual(result, f"mock_{provider}")
                mock_method.assert_called_once_with(config)

    def test_create_transcriber_invalid_provider(self):
        """Test error raised when invalid transcriber provider requested"""
        factory = mpf.VoiceComponentFactory()
        config = {"transcriberProvider": "unsupported_transcriber"}
        with self.assertRaises(ValueError) as ctx:
            factory.create_transcriber(config)
        self.assertIn("Unknown transcriber provider: unsupported_transcriber", str(ctx.exception))

    def test_create_transcriber_default_provider(self):
        """Test default transcriber provider (deepgram) when key is missing"""
        config = {}
        with patch.object(mpf.VoiceComponentFactory, "_create_deepgram_transcriber", return_value="mock_deepgram") as mock_method:
            factory = mpf.VoiceComponentFactory()
            result = factory.create_transcriber(config)
            self.assertEqual(result, "mock_deepgram")
            mock_method.assert_called_once_with(config)

    def test_create_agent_valid_providers(self):
        """Test creating agents for supported LLM providers"""
        providers = ["openai", "gemini", "claude"]
        for provider in providers:
            config = {"llmProvider": provider}
            method_name = f"_create_{provider}_agent"
            with patch.object(mpf.VoiceComponentFactory, method_name, return_value=f"mock_{provider}") as mock_method:
                factory = mpf.VoiceComponentFactory()
                result = factory.create_agent(config)
                self.assertEqual(result, f"mock_{provider}")
                mock_method.assert_called_once_with(config)

    def test_create_agent_invalid_provider(self):
        """Test error raised when invalid LLM provider requested"""
        factory = mpf.VoiceComponentFactory()
        config = {"llmProvider": "unsupported_llm"}
        with self.assertRaises(ValueError) as ctx:
            factory.create_agent(config)
        self.assertIn("Unknown LLM provider: unsupported_llm", str(ctx.exception))

    def test_create_agent_default_provider(self):
        """Test default LLM provider (openai) when key is missing"""
        config = {}
        with patch.object(mpf.VoiceComponentFactory, "_create_openai_agent", return_value="mock_openai") as mock_method:
            factory = mpf.VoiceComponentFactory()
            result = factory.create_agent(config)
            self.assertEqual(result, "mock_openai")
            mock_method.assert_called_once_with(config)

    def test_create_synthesizer_valid_providers(self):
        """Test creating synthesizers for supported TTS providers"""
        providers = ["elevenlabs", "azure", "google", "polly", "playht"]
        for provider in providers:
            config = {"voiceProvider": provider}
            method_name = f"_create_{provider}_synthesizer"
            with patch.object(mpf.VoiceComponentFactory, method_name, return_value=f"mock_{provider}") as mock_method:
                factory = mpf.VoiceComponentFactory()
                result = factory.create_synthesizer(config)
                self.assertEqual(result, f"mock_{provider}")
                mock_method.assert_called_once_with(config)

    def test_create_synthesizer_invalid_provider(self):
        """Test error raised when invalid voice provider requested"""
        factory = mpf.VoiceComponentFactory()
        config = {"voiceProvider": "unsupported_voice"}
        with self.assertRaises(ValueError) as ctx:
            factory.create_synthesizer(config)
        self.assertIn("Unknown voice provider: unsupported_voice", str(ctx.exception))

    def test_create_synthesizer_default_provider(self):
        """Test default voice provider (elevenlabs) when key is missing"""
        config = {}
        with patch.object(mpf.VoiceComponentFactory, "_create_elevenlabs_synthesizer", return_value="mock_elevenlabs") as mock_method:
            factory = mpf.VoiceComponentFactory()
            result = factory.create_synthesizer(config)
            self.assertEqual(result, "mock_elevenlabs")
            mock_method.assert_called_once_with(config)


class TestUnimplementedMethods(unittest.TestCase):
    """Unit tests verifying template methods raise NotImplementedError"""

    def setUp(self):
        self.factory = mpf.VoiceComponentFactory()
        self.dummy_config = {}

    def test_transcriber_unimplemented_methods(self):
        methods = [
            self.factory._create_deepgram_transcriber,
            self.factory._create_assemblyai_transcriber,
            self.factory._create_azure_transcriber,
            self.factory._create_google_transcriber,
        ]
        for method in methods:
            with self.assertRaises(NotImplementedError):
                method(self.dummy_config)

    def test_agent_unimplemented_methods(self):
        methods = [
            self.factory._create_openai_agent,
            self.factory._create_gemini_agent,
            self.factory._create_claude_agent,
        ]
        for method in methods:
            with self.assertRaises(NotImplementedError):
                method(self.dummy_config)

    def test_synthesizer_unimplemented_methods(self):
        methods = [
            self.factory._create_elevenlabs_synthesizer,
            self.factory._create_azure_synthesizer,
            self.factory._create_google_synthesizer,
            self.factory._create_polly_synthesizer,
            self.factory._create_playht_synthesizer,
        ]
        for method in methods:
            with self.assertRaises(NotImplementedError):
                method(self.dummy_config)


class TestProviderInterfaces(unittest.TestCase):
    """Unit tests for Provider Abstract Base Classes"""

    def test_transcriber_provider_abstract(self):
        with self.assertRaises(TypeError):
            mpf.TranscriberProvider()

    def test_llm_provider_abstract(self):
        with self.assertRaises(TypeError):
            mpf.LLMProvider()

    def test_tts_provider_abstract(self):
        with self.assertRaises(TypeError):
            mpf.TTSProvider()


if __name__ == "__main__":
    unittest.main()
