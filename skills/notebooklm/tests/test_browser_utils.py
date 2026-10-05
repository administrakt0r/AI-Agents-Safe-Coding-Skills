"""
Tests for BrowserFactory._inject_cookies in skills/notebooklm/scripts/browser_utils.py
"""

import sys
from pathlib import Path
from unittest.mock import MagicMock, patch, mock_open

# Ensure patchright can be imported even if not installed in the environment
try:
    import patchright
except ImportError:
    mock_patchright = MagicMock()
    sys.modules["patchright"] = mock_patchright
    sys.modules["patchright.sync_api"] = mock_patchright

# Add scripts directory to path to import browser_utils and config
scripts_dir = Path(__file__).parent.parent / "scripts"
if str(scripts_dir) not in sys.path:
    sys.path.insert(0, str(scripts_dir))

from browser_utils import BrowserFactory


def test_inject_cookies_file_not_exists():
    """Test _inject_cookies when STATE_FILE does not exist."""
    context = MagicMock()
    with patch("browser_utils.STATE_FILE") as mock_state_file:
        mock_state_file.exists.return_value = False
        BrowserFactory._inject_cookies(context)
        context.add_cookies.assert_not_called()


def test_inject_cookies_success():
    """Test _inject_cookies when STATE_FILE exists and contains valid cookies."""
    context = MagicMock()
    fake_json_data = '{"cookies": [{"name": "session", "value": "xyz"}]}'

    with patch("browser_utils.STATE_FILE") as mock_state_file:
        mock_state_file.exists.return_value = True
        with patch("builtins.open", mock_open(read_data=fake_json_data)):
            BrowserFactory._inject_cookies(context)
            context.add_cookies.assert_called_once_with([{"name": "session", "value": "xyz"}])


def test_inject_cookies_empty_cookies():
    """Test _inject_cookies when STATE_FILE exists but cookies list is empty."""
    context = MagicMock()
    fake_json_data = '{"cookies": []}'

    with patch("browser_utils.STATE_FILE") as mock_state_file:
        mock_state_file.exists.return_value = True
        with patch("builtins.open", mock_open(read_data=fake_json_data)):
            BrowserFactory._inject_cookies(context)
            context.add_cookies.assert_not_called()


def test_inject_cookies_error_path(capsys):
    """
    Test error path in _inject_cookies when reading state.json raises an exception
    (e.g., corrupt JSON or file read error).
    Verifies graceful handling, error print output, and no raised exception.
    """
    context = MagicMock()

    with patch("browser_utils.STATE_FILE") as mock_state_file:
        mock_state_file.exists.return_value = True
        with patch("builtins.open", side_effect=Exception("Disk read error")):
            # Should catch exception gracefully and not crash
            BrowserFactory._inject_cookies(context)

            # Check printed output warning
            captured = capsys.readouterr()
            assert "⚠️  Could not load state.json: Disk read error" in captured.out
            context.add_cookies.assert_not_called()


def test_inject_cookies_json_decode_error(capsys):
    """
    Test error path when STATE_FILE contains invalid JSON.
    """
    context = MagicMock()
    invalid_json_data = "{ invalid json }"

    with patch("browser_utils.STATE_FILE") as mock_state_file:
        mock_state_file.exists.return_value = True
        with patch("builtins.open", mock_open(read_data=invalid_json_data)):
            BrowserFactory._inject_cookies(context)

            captured = capsys.readouterr()
            assert "⚠️  Could not load state.json:" in captured.out
            context.add_cookies.assert_not_called()
