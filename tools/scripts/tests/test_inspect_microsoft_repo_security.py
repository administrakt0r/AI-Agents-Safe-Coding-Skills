import ast
import sys
import unittest
from pathlib import Path
from unittest.mock import patch, MagicMock

TOOLS_SCRIPTS_TESTS_DIR = Path(__file__).resolve().parent
if str(TOOLS_SCRIPTS_TESTS_DIR) not in sys.path:
    sys.path.insert(0, str(TOOLS_SCRIPTS_TESTS_DIR))

import inspect_microsoft_repo


class TestInspectMicrosoftRepoSecurity(unittest.TestCase):
    def test_subprocess_calls_use_list_args_and_no_shell(self):
        """Ensure subprocess.run is called with a list of args and shell=False (or shell omitted/False)."""
        target_file = TOOLS_SCRIPTS_TESTS_DIR / "inspect_microsoft_repo.py"
        content = target_file.read_text(encoding="utf-8")
        parsed = ast.parse(content)

        subprocess_calls = []
        for node in ast.walk(parsed):
            if isinstance(node, ast.Call):
                if isinstance(node.func, ast.Attribute) and node.func.attr == "run":
                    if isinstance(node.func.value, ast.Name) and node.func.value.id == "subprocess":
                        subprocess_calls.append(node)

        self.assertGreater(len(subprocess_calls), 0, "Expected at least one subprocess.run call")

        for call in subprocess_calls:
            # Check first argument is a list or variable
            first_arg = call.args[0]
            self.assertIsInstance(
                first_arg,
                (ast.List, ast.Name),
                "Subprocess command should be passed as a list of arguments, not a string"
            )

            # Check keywords for shell argument
            for keyword in call.keywords:
                if keyword.arg == "shell":
                    self.assertIsInstance(keyword.value, ast.Constant)
                    self.assertFalse(
                        keyword.value.value,
                        "subprocess.run shell argument must be False"
                    )

    @patch("subprocess.run")
    @patch("shutil.rmtree")
    def test_inspect_repo_executes_git_clone_safely(self, mock_rmtree, mock_subprocess_run):
        """Mock subprocess.run and verify git clone call arguments."""
        mock_subprocess_run.return_value = MagicMock(returncode=0)

        # Patch Path.rglob to return empty list to avoid processing cloned files
        with patch.object(Path, "rglob", return_value=[]):
            inspect_microsoft_repo.inspect_repo()

        self.assertTrue(mock_subprocess_run.called)
        args, kwargs = mock_subprocess_run.call_args
        cmd = args[0]

        # Verify command is a list starting with 'git'
        self.assertIsInstance(cmd, list)
        self.assertEqual(cmd[0], "git")
        self.assertEqual(cmd[1], "clone")

        # Verify shell is False or not enabled
        self.assertFalse(kwargs.get("shell", False))


if __name__ == "__main__":
    unittest.main()
