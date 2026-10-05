import sys
from pathlib import Path
from unittest.mock import patch

# Add parent directory of tests (scripts) to path so auth_manager can be imported
sys.path.insert(0, str(Path(__file__).parent.parent / "scripts"))

from auth_manager import _get_hostname, _is_exact_host


def test_get_hostname_valid():
    """Test _get_hostname with valid standard URLs."""
    assert _get_hostname("https://notebooklm.google.com/a/b") == "notebooklm.google.com"
    assert _get_hostname("HTTP://EXAMPLE.COM:8080/path") == "example.com"


def test_get_hostname_empty_or_none_hostname():
    """Test _get_hostname when URL has no hostname."""
    assert _get_hostname("relative/path") == ""
    assert _get_hostname("http://") == ""


def test_get_hostname_value_error_exception():
    """Test _get_hostname error path when urlparse raises ValueError."""
    # Invalid bracketed netloc triggers ValueError in urlparse/urlsplit (_check_bracketed_host)
    invalid_url = "http://[invalid-ipv6]"
    assert _get_hostname(invalid_url) == ""

    # Mock urlparse to explicitly verify ValueError exception handling
    with patch("auth_manager.urlparse", side_effect=ValueError("Invalid URL")):
        assert _get_hostname("https://notebooklm.google.com") == ""


def test_is_exact_host():
    """Test _is_exact_host function."""
    assert _is_exact_host("https://notebooklm.google.com/path", "notebooklm.google.com") is True
    assert _is_exact_host("https://sub.notebooklm.google.com/path", "notebooklm.google.com") is False
    assert _is_exact_host("http://[invalid-ipv6]", "notebooklm.google.com") is False
