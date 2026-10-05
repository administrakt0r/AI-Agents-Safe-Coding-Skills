"""Tests for browser_session module in skills/notebooklm/scripts."""

import sys
import unittest
from pathlib import Path
from unittest.mock import MagicMock, patch

# Ensure patchright modules can be imported/mocked if not installed in environment
if "patchright" not in sys.modules:
    mock_patchright = MagicMock()
    sys.modules["patchright"] = mock_patchright
    sys.modules["patchright.sync_api"] = mock_patchright.sync_api

# Add scripts directory to path
sys.path.insert(0, str(Path(__file__).parent.parent / "scripts"))

import browser_session
from browser_session import BrowserSession, _get_hostname


class TestGetHostname(unittest.TestCase):
    def test_valid_urls(self):
        self.assertEqual(_get_hostname("https://notebooklm.google.com/notebook/123"), "notebooklm.google.com")
        self.assertEqual(_get_hostname("https://ACCOUNTS.GOOGLE.COM/signin"), "accounts.google.com")

    def test_invalid_url_value_error(self):
        # urlparse on invalid bracketed host raises ValueError
        self.assertEqual(_get_hostname("http://[invalid_ipv6]"), "")


class TestBrowserSessionInit(unittest.TestCase):
    def setUp(self):
        self.mock_context = MagicMock()
        self.mock_page = MagicMock()
        self.mock_context.new_page.return_value = self.mock_page

    @patch.object(BrowserSession, "_wait_for_ready")
    @patch("browser_session.StealthUtils")
    def test_initialize_auth_required_raises_error(self, mock_stealth, mock_wait_for_ready):
        self.mock_page.url = "https://accounts.google.com/v3/signin"

        with self.assertRaises(RuntimeError) as cm:
            BrowserSession("session-1", self.mock_context, "https://notebooklm.google.com/notebook/123")

        self.assertIn("Authentication required", str(cm.exception))
        self.mock_page.close.assert_called_once()

    @patch("browser_session.StealthUtils")
    def test_initialize_goto_exception_handled_and_page_closed(self, mock_stealth):
        self.mock_page.goto.side_effect = Exception("Network timeout")

        with self.assertRaises(Exception) as cm:
            BrowserSession("session-1", self.mock_context, "https://notebooklm.google.com/notebook/123")

        self.assertIn("Network timeout", str(cm.exception))
        self.mock_page.close.assert_called_once()


class TestBrowserSessionWaitForReady(unittest.TestCase):
    def setUp(self):
        self.mock_context = MagicMock()
        self.mock_page = MagicMock()
        self.mock_context.new_page.return_value = self.mock_page

    @patch.object(BrowserSession, "_initialize")
    def test_wait_for_ready_fallback_selector(self, mock_init):
        session = BrowserSession("session-1", self.mock_context, "https://notebooklm.google.com/notebook/123")
        session.page = self.mock_page

        # First wait_for_selector call raises exception, second succeeds
        self.mock_page.wait_for_selector.side_effect = [
            Exception("Primary selector timeout"),
            MagicMock(),
        ]

        session._wait_for_ready()

        self.assertEqual(self.mock_page.wait_for_selector.call_count, 2)
        self.mock_page.wait_for_selector.assert_called_with(
            'textarea[aria-label="Feld für Anfragen"]', timeout=5000, state="visible"
        )


class TestBrowserSessionAsk(unittest.TestCase):
    def setUp(self):
        self.mock_context = MagicMock()
        self.mock_page = MagicMock()
        self.mock_context.new_page.return_value = self.mock_page

    @patch.object(BrowserSession, "_initialize")
    @patch.object(BrowserSession, "_snapshot_latest_response", return_value="prev response")
    @patch.object(BrowserSession, "_wait_for_latest_answer", return_value="")
    def test_ask_empty_response_returns_error_dict(self, mock_wait_answer, mock_snapshot, mock_init):
        session = BrowserSession("session-1", self.mock_context, "https://notebooklm.google.com/notebook/123")
        session.page = self.mock_page

        res = session.ask("What is this notebook about?")

        self.assertEqual(res["status"], "error")
        self.assertEqual(res["error"], "Empty response from NotebookLM")
        self.assertEqual(res["question"], "What is this notebook about?")

    @patch.object(BrowserSession, "_initialize")
    def test_ask_exception_during_typing_returns_error_dict(self, mock_init):
        session = BrowserSession("session-1", self.mock_context, "https://notebooklm.google.com/notebook/123")
        session.page = self.mock_page
        self.mock_page.wait_for_selector.side_effect = Exception("Input field not found")

        res = session.ask("Hello?")

        self.assertEqual(res["status"], "error")
        self.assertIn("Input field not found", res["error"])


class TestBrowserSessionSnapshotAndWaitAnswer(unittest.TestCase):
    def setUp(self):
        self.mock_context = MagicMock()
        self.mock_page = MagicMock()
        self.mock_context.new_page.return_value = self.mock_page

    @patch.object(BrowserSession, "_initialize")
    def test_snapshot_latest_response_exception_returns_none(self, mock_init):
        session = BrowserSession("session-1", self.mock_context, "https://notebooklm.google.com/notebook/123")
        session.page = self.mock_page
        self.mock_page.query_selector_all.side_effect = Exception("DOM error")

        snapshot = session._snapshot_latest_response()
        self.assertIsNone(snapshot)

    @patch.object(BrowserSession, "_initialize")
    def test_wait_for_latest_answer_timeout_raises_exception(self, mock_init):
        session = BrowserSession("session-1", self.mock_context, "https://notebooklm.google.com/notebook/123")
        session.page = self.mock_page
        self.mock_page.query_selector.return_value = None
        self.mock_page.query_selector_all.return_value = []

        with self.assertRaises(TimeoutError) as cm:
            session._wait_for_latest_answer(previous_answer=None, timeout=1)

        self.assertIn("No response received within 1 seconds", str(cm.exception))


class TestBrowserSessionClose(unittest.TestCase):
    def setUp(self):
        self.mock_context = MagicMock()
        self.mock_page = MagicMock()
        self.mock_context.new_page.return_value = self.mock_page

    @patch.object(BrowserSession, "_initialize")
    def test_close_handles_exception_gracefully(self, mock_init):
        session = BrowserSession("session-1", self.mock_context, "https://notebooklm.google.com/notebook/123")
        session.page = self.mock_page
        self.mock_page.close.side_effect = Exception("Already closed")

        # Calling close should handle exception without raising
        session.close()
        self.mock_page.close.assert_called_once()


if __name__ == "__main__":
    unittest.main()
