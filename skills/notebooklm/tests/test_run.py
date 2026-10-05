"""Tests for skills/notebooklm/scripts/run.py"""

import sys
import unittest
from pathlib import Path
from unittest.mock import MagicMock, patch

# Add scripts directory to path so run module can be imported
skill_scripts_dir = Path(__file__).parent.parent / "scripts"
sys.path.insert(0, str(skill_scripts_dir))

import run  # noqa: E402


class TestGetVenvPython(unittest.TestCase):
    """Test get_venv_python function across operating systems."""

    @patch("run.os.name", "posix")
    def test_get_venv_python_unix(self):
        """Test get_venv_python returns correct path on Unix/Linux/Mac."""
        venv_python = run.get_venv_python()
        expected = Path(run.__file__).parent.parent / ".venv" / "bin" / "python"
        self.assertEqual(venv_python, expected)

    @patch("run.os.name", "nt")
    @patch("run.Path")
    def test_get_venv_python_windows(self, mock_path):
        """Test get_venv_python returns correct path on Windows."""
        mock_skill_dir = MagicMock()
        mock_path.return_value.parent.parent = mock_skill_dir

        venv_python = run.get_venv_python()
        expected = mock_skill_dir / ".venv" / "Scripts" / "python.exe"

        self.assertEqual(venv_python, expected)


class TestEnsureVenv(unittest.TestCase):
    """Test ensure_venv function behavior."""

    @patch.object(Path, "exists", return_value=True)
    def test_ensure_venv_exists(self, mock_exists):
        """Test ensure_venv when virtualenv directory already exists."""
        venv_python = run.ensure_venv()
        expected = run.get_venv_python()
        self.assertEqual(venv_python, expected)

    @patch("subprocess.run")
    @patch.object(Path, "exists", return_value=False)
    def test_ensure_venv_creates_and_succeeds(self, mock_exists, mock_subprocess):
        """Test ensure_venv when venv does not exist and setup script succeeds."""
        mock_subprocess.return_value = MagicMock(returncode=0)

        venv_python = run.ensure_venv()
        expected = run.get_venv_python()

        self.assertEqual(venv_python, expected)
        mock_subprocess.assert_called_once()

    @patch("subprocess.run")
    @patch.object(Path, "exists", return_value=False)
    def test_ensure_venv_fails(self, mock_exists, mock_subprocess):
        """Test ensure_venv exits on setup script failure."""
        mock_subprocess.return_value = MagicMock(returncode=1)

        with self.assertRaises(SystemExit) as cm:
            run.ensure_venv()
        self.assertEqual(cm.exception.code, 1)


class TestMain(unittest.TestCase):
    """Test main function handling of arguments and script execution."""

    @patch("sys.argv", ["run.py"])
    def test_main_no_args(self):
        """Test main exits with 1 when no script argument provided."""
        with self.assertRaises(SystemExit) as cm:
            run.main()
        self.assertEqual(cm.exception.code, 1)

    @patch("run.ensure_venv")
    @patch.object(Path, "exists", return_value=False)
    @patch("sys.argv", ["run.py", "nonexistent_script.py"])
    def test_main_script_not_found(self, mock_exists, mock_ensure_venv):
        """Test main exits with 1 when specified script does not exist."""
        with self.assertRaises(SystemExit) as cm:
            run.main()
        self.assertEqual(cm.exception.code, 1)

    @patch("subprocess.run")
    @patch("run.ensure_venv")
    @patch.object(Path, "exists", return_value=True)
    @patch("sys.argv", ["run.py", "ask_question.py", "--query", "hello"])
    def test_main_runs_script(self, mock_exists, mock_ensure_venv, mock_subprocess):
        """Test main runs script with venv python when script exists."""
        mock_ensure_venv.return_value = Path("/fake/venv/bin/python")
        mock_subprocess.return_value = MagicMock(returncode=0)

        with self.assertRaises(SystemExit) as cm:
            run.main()

        mock_subprocess.assert_called_once()
        self.assertEqual(cm.exception.code, 0)

    @patch("subprocess.run")
    @patch("run.ensure_venv")
    @patch.object(Path, "exists", return_value=True)
    @patch("sys.argv", ["run.py", "scripts/ask_question"])
    def test_main_normalizes_script_name(self, mock_exists, mock_ensure_venv, mock_subprocess):
        """Test main strips 'scripts/' prefix and adds '.py' extension."""
        mock_ensure_venv.return_value = Path("/fake/venv/bin/python")
        mock_subprocess.return_value = MagicMock(returncode=0)

        with self.assertRaises(SystemExit) as cm:
            run.main()

        mock_subprocess.assert_called_once()
        cmd = mock_subprocess.call_args[0][0]
        self.assertTrue(cmd[1].endswith("ask_question.py"))
        self.assertEqual(cm.exception.code, 0)


if __name__ == "__main__":
    unittest.main()
