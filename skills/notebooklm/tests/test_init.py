"""
Unit tests for skills/notebooklm/scripts/__init__.py
"""

import os
import sys
import unittest
from pathlib import Path, PosixPath
from unittest.mock import MagicMock, patch

# Ensure repo root and skills/notebooklm/scripts directory are importable
REPO_ROOT = Path(__file__).parent.parent.parent.parent
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

SKILL_DIR = Path(__file__).parent.parent
SCRIPTS_DIR = SKILL_DIR / "scripts"
if str(SCRIPTS_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPTS_DIR))

# Import target function
from skills.notebooklm.scripts import ensure_venv_and_run


class TestEnsureVenvAndRun(unittest.TestCase):
    def setUp(self):
        self.skill_dir = SKILL_DIR
        self.venv_dir = self.skill_dir / ".venv"
        self.requirements_file = self.skill_dir / "requirements.txt"

    def test_already_in_target_venv(self):
        """Test early return when already in the skill's virtual environment."""
        with patch.object(sys, "prefix", str(self.venv_dir)), patch.object(
            sys, "real_prefix", str(self.venv_dir), create=True
        ):
            with patch("pathlib.Path.exists") as mock_exists, patch(
                "subprocess.run"
            ) as mock_run:
                ensure_venv_and_run()
                mock_run.assert_not_called()

    @patch("subprocess.run")
    @patch("venv.create")
    def test_venv_exists_not_in_venv(self, mock_venv_create, mock_run):
        """Test when .venv already exists but process is running outside venv."""
        with patch.object(sys, "prefix", "/usr/local"), patch.object(
            sys, "base_prefix", "/usr/local"
        ):
            if hasattr(sys, "real_prefix"):
                delattr(sys, "real_prefix")

            with patch("pathlib.Path.exists", return_value=True):
                ensure_venv_and_run()
                mock_venv_create.assert_not_called()
                mock_run.assert_not_called()

    @patch("subprocess.run")
    @patch("venv.create")
    def test_create_venv_posix(self, mock_venv_create, mock_run):
        """Test creating venv and installing requirements on POSIX systems."""
        with patch.object(sys, "prefix", "/usr/local"), patch.object(
            sys, "base_prefix", "/usr/local"
        ), patch("os.name", "posix"):
            if hasattr(sys, "real_prefix"):
                delattr(sys, "real_prefix")

            def exists_side_effect(path_self):
                if path_self == self.venv_dir:
                    return False
                if path_self == self.requirements_file:
                    return True
                return False

            with patch("pathlib.Path.exists", autospec=True, side_effect=exists_side_effect):
                ensure_venv_and_run()

                mock_venv_create.assert_called_once_with(
                    self.venv_dir, with_pip=True
                )
                self.assertEqual(mock_run.call_count, 2)

                # First call to pip install
                pip_exe = str(self.venv_dir / "bin" / "pip")
                req_file = str(self.requirements_file)
                mock_run.assert_any_call(
                    [pip_exe, "install", "-q", "-r", req_file], check=True
                )

                # Second call to patchright install chromium
                python_exe = str(self.venv_dir / "bin" / "python")
                mock_run.assert_any_call(
                    [python_exe, "-m", "patchright", "install", "chromium"],
                    check=True,
                    capture_output=True,
                )

    @patch("subprocess.run")
    @patch("venv.create")
    def test_create_venv_windows(self, mock_venv_create, mock_run):
        """Test creating venv and installing requirements on Windows systems."""
        with patch.object(sys, "prefix", "/usr/local"), patch.object(
            sys, "base_prefix", "/usr/local"
        ), patch("os.name", "nt"), patch("skills.notebooklm.scripts.Path", PosixPath):
            if hasattr(sys, "real_prefix"):
                delattr(sys, "real_prefix")

            def exists_side_effect(path_self):
                if path_self == self.venv_dir:
                    return False
                if path_self == self.requirements_file:
                    return True
                return False

            with patch("pathlib.Path.exists", autospec=True, side_effect=exists_side_effect):
                ensure_venv_and_run()

                mock_venv_create.assert_called_once_with(
                    self.venv_dir, with_pip=True
                )
                self.assertEqual(mock_run.call_count, 2)

                pip_exe = str(self.venv_dir / "Scripts" / "pip.exe")
                req_file = str(self.requirements_file)
                mock_run.assert_any_call(
                    [pip_exe, "install", "-q", "-r", req_file], check=True
                )

                python_exe = str(self.venv_dir / "Scripts" / "python.exe")
                mock_run.assert_any_call(
                    [python_exe, "-m", "patchright", "install", "chromium"],
                    check=True,
                    capture_output=True,
                )

    @patch("subprocess.run")
    @patch("venv.create")
    def test_create_venv_no_requirements(self, mock_venv_create, mock_run):
        """Test creating venv when requirements.txt does not exist."""
        with patch.object(sys, "prefix", "/usr/local"), patch.object(
            sys, "base_prefix", "/usr/local"
        ):
            if hasattr(sys, "real_prefix"):
                delattr(sys, "real_prefix")

            with patch("pathlib.Path.exists", return_value=False):
                ensure_venv_and_run()

                mock_venv_create.assert_called_once_with(
                    self.venv_dir, with_pip=True
                )
                mock_run.assert_not_called()


if __name__ == "__main__":
    unittest.main()
