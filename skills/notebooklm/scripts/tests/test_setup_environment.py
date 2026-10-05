"""
Tests for setup_environment.py in skills/notebooklm/scripts
"""

import os
import sys
import pytest
import subprocess
from pathlib import Path
from unittest.mock import Mock, patch, MagicMock

# Add scripts directory to path so we can import setup_environment
sys.path.insert(0, str(Path(__file__).parent.parent))

from setup_environment import SkillEnvironment, main


class TestSkillEnvironment:
    """Test SkillEnvironment class."""

    @pytest.fixture
    def env(self):
        """Fixture for SkillEnvironment instance."""
        return SkillEnvironment()

    def test_init_paths(self, env):
        """Test initialization of paths."""
        assert env.skill_dir.name == "notebooklm"
        assert env.venv_dir == env.skill_dir / ".venv"
        assert env.requirements_file == env.skill_dir / "requirements.txt"

        if os.name == 'nt':
            assert env.venv_python == env.venv_dir / "Scripts" / "python.exe"
            assert env.venv_pip == env.venv_dir / "Scripts" / "pip.exe"
        else:
            assert env.venv_python == env.venv_dir / "bin" / "python"
            assert env.venv_pip == env.venv_dir / "bin" / "pip"

    def test_is_in_skill_venv_true(self, env, monkeypatch):
        """Test is_in_skill_venv when running inside the skill's venv."""
        monkeypatch.setattr(sys, 'prefix', str(env.venv_dir))
        monkeypatch.setattr(sys, 'base_prefix', str(env.skill_dir))
        assert env.is_in_skill_venv() is True

    def test_is_in_skill_venv_false_not_in_venv(self, env, monkeypatch):
        """Test is_in_skill_venv when not in any venv."""
        if hasattr(sys, 'real_prefix'):
            monkeypatch.delattr(sys, 'real_prefix')
        monkeypatch.setattr(sys, 'base_prefix', sys.prefix)
        assert env.is_in_skill_venv() is False

    def test_is_in_skill_venv_false_different_venv(self, env, monkeypatch, tmp_path):
        """Test is_in_skill_venv when in a different venv."""
        monkeypatch.setattr(sys, 'prefix', str(tmp_path / "other_venv"))
        monkeypatch.setattr(sys, 'base_prefix', str(tmp_path))
        assert env.is_in_skill_venv() is False

    def test_get_python_executable_exists(self, env, monkeypatch, tmp_path):
        """Test get_python_executable when venv python exists."""
        fake_python = tmp_path / "python"
        fake_python.touch()
        monkeypatch.setattr(env, 'venv_python', fake_python)
        assert env.get_python_executable() == str(fake_python)

    def test_get_python_executable_not_exists(self, env, monkeypatch, tmp_path):
        """Test get_python_executable when venv python does not exist."""
        fake_python = tmp_path / "nonexistent_python"
        monkeypatch.setattr(env, 'venv_python', fake_python)
        assert env.get_python_executable() == sys.executable

    def test_activate_instructions_nt(self, env, monkeypatch):
        """Test activate_instructions on Windows."""
        monkeypatch.setattr(os, 'name', 'nt')
        instructions = env.activate_instructions()
        assert "activate.bat" in instructions
        assert instructions.startswith("Run: ")

    def test_activate_instructions_posix(self, env, monkeypatch):
        """Test activate_instructions on Unix/Linux/Mac."""
        monkeypatch.setattr(os, 'name', 'posix')
        instructions = env.activate_instructions()
        assert "activate" in instructions
        assert instructions.startswith("Run: source ")

    def test_ensure_venv_already_in_venv(self, env, monkeypatch):
        """Test ensure_venv when already in skill venv."""
        monkeypatch.setattr(env, 'is_in_skill_venv', lambda: True)
        assert env.ensure_venv() is True

    def test_ensure_venv_creation_failure(self, env, monkeypatch, tmp_path):
        """Test ensure_venv error path when venv creation fails."""
        monkeypatch.setattr(env, 'is_in_skill_venv', lambda: False)
        monkeypatch.setattr(env, 'venv_dir', tmp_path / "nonexistent_dir")

        with patch('venv.create', side_effect=Exception("Permission denied")):
            assert env.ensure_venv() is False

    def test_ensure_venv_no_requirements_file(self, env, monkeypatch, tmp_path):
        """Test ensure_venv when requirements.txt does not exist."""
        monkeypatch.setattr(env, 'is_in_skill_venv', lambda: False)
        monkeypatch.setattr(env, 'venv_dir', tmp_path / "venv")

        fake_req = tmp_path / "no_requirements.txt"
        monkeypatch.setattr(env, 'requirements_file', fake_req)

        with patch('venv.create'):
            assert env.ensure_venv() is True

    def test_ensure_venv_dependency_install_failure(self, env, monkeypatch, tmp_path):
        """Test ensure_venv error path when dependency installation fails."""
        monkeypatch.setattr(env, 'is_in_skill_venv', lambda: False)
        monkeypatch.setattr(env, 'venv_dir', tmp_path / "venv")

        fake_req = tmp_path / "requirements.txt"
        fake_req.touch()
        monkeypatch.setattr(env, 'requirements_file', fake_req)

        with patch('venv.create'):
            with patch('subprocess.run', side_effect=subprocess.CalledProcessError(1, 'pip install', output='error')):
                assert env.ensure_venv() is False

    def test_ensure_venv_chrome_install_warning(self, env, monkeypatch, tmp_path):
        """Test ensure_venv when Chrome install raises CalledProcessError but continues."""
        monkeypatch.setattr(env, 'is_in_skill_venv', lambda: False)
        monkeypatch.setattr(env, 'venv_dir', tmp_path / "venv")

        fake_req = tmp_path / "requirements.txt"
        fake_req.touch()
        monkeypatch.setattr(env, 'requirements_file', fake_req)

        def mock_subprocess_run(cmd, **kwargs):
            if "patchright" in cmd:
                raise subprocess.CalledProcessError(1, cmd, output="Chrome install error")
            return subprocess.CompletedProcess(cmd, 0)

        with patch('venv.create'):
            with patch('subprocess.run', side_effect=mock_subprocess_run):
                assert env.ensure_venv() is True

    def test_ensure_venv_success(self, env, monkeypatch, tmp_path):
        """Test ensure_venv happy path."""
        monkeypatch.setattr(env, 'is_in_skill_venv', lambda: False)
        monkeypatch.setattr(env, 'venv_dir', tmp_path / "venv")

        fake_req = tmp_path / "requirements.txt"
        fake_req.touch()
        monkeypatch.setattr(env, 'requirements_file', fake_req)

        with patch('venv.create'):
            with patch('subprocess.run', return_value=subprocess.CompletedProcess([], 0)):
                assert env.ensure_venv() is True

    def test_run_script_not_found(self, env, tmp_path, monkeypatch):
        """Test run_script when script file does not exist."""
        monkeypatch.setattr(env, 'skill_dir', tmp_path)
        assert env.run_script("nonexistent.py") == 1

    def test_run_script_ensure_venv_fails(self, env, tmp_path, monkeypatch):
        """Test run_script when ensure_venv returns False."""
        script_dir = tmp_path / "scripts"
        script_dir.mkdir()
        script_file = script_dir / "test_script.py"
        script_file.touch()

        monkeypatch.setattr(env, 'skill_dir', tmp_path)
        monkeypatch.setattr(env, 'ensure_venv', lambda: False)

        assert env.run_script("test_script.py") == 1

    def test_run_script_success(self, env, tmp_path, monkeypatch):
        """Test run_script execution success."""
        script_dir = tmp_path / "scripts"
        script_dir.mkdir()
        script_file = script_dir / "test_script.py"
        script_file.touch()

        monkeypatch.setattr(env, 'skill_dir', tmp_path)
        monkeypatch.setattr(env, 'ensure_venv', lambda: True)

        with patch('subprocess.run', return_value=subprocess.CompletedProcess([], 0)):
            assert env.run_script("test_script.py", ["--arg1"]) == 0

    def test_run_script_exception(self, env, tmp_path, monkeypatch):
        """Test run_script error path when subprocess raises an exception."""
        script_dir = tmp_path / "scripts"
        script_dir.mkdir()
        script_file = script_dir / "test_script.py"
        script_file.touch()

        monkeypatch.setattr(env, 'skill_dir', tmp_path)
        monkeypatch.setattr(env, 'ensure_venv', lambda: True)

        with patch('subprocess.run', side_effect=Exception("Subprocess error")):
            assert env.run_script("test_script.py") == 1


class TestMain:
    """Test main function and CLI arguments."""

    @patch('setup_environment.SkillEnvironment')
    def test_main_check_venv_exists(self, mock_env_cls):
        """Test main with --check flag when venv exists."""
        mock_env = mock_env_cls.return_value
        mock_env.venv_dir.exists.return_value = True

        with patch('sys.argv', ['setup_environment.py', '--check']):
            result = main()
            assert result is None or result == 0

    @patch('setup_environment.SkillEnvironment')
    def test_main_check_venv_not_exists(self, mock_env_cls):
        """Test main with --check flag when venv does not exist."""
        mock_env = mock_env_cls.return_value
        mock_env.venv_dir.exists.return_value = False

        with patch('sys.argv', ['setup_environment.py', '--check']):
            result = main()
            assert result is None or result == 0

    @patch('setup_environment.SkillEnvironment')
    def test_main_run_option(self, mock_env_cls):
        """Test main with --run flag."""
        mock_env = mock_env_cls.return_value
        mock_env.run_script.return_value = 0

        with patch('sys.argv', ['setup_environment.py', '--run', 'ask_question.py', 'arg1']):
            result = main()
            assert result == 0
            mock_env.run_script.assert_called_once_with('ask_question.py', ['arg1'])

    @patch('setup_environment.SkillEnvironment')
    def test_main_default_success(self, mock_env_cls):
        """Test main default invocation when ensure_venv succeeds."""
        mock_env = mock_env_cls.return_value
        mock_env.ensure_venv.return_value = True

        with patch('sys.argv', ['setup_environment.py']):
            result = main()
            assert result is None or result == 0

    @patch('setup_environment.SkillEnvironment')
    def test_main_default_failure(self, mock_env_cls):
        """Test main default invocation when ensure_venv fails."""
        mock_env = mock_env_cls.return_value
        mock_env.ensure_venv.return_value = False

        with patch('sys.argv', ['setup_environment.py']):
            result = main()
            assert result == 1
