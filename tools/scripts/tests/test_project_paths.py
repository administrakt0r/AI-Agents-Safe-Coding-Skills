import sys
import tempfile
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[3]
TOOLS_SCRIPTS_DIR = REPO_ROOT / "tools" / "scripts"
if str(TOOLS_SCRIPTS_DIR) not in sys.path:
    sys.path.insert(0, str(TOOLS_SCRIPTS_DIR))

from _project_paths import find_repo_root


class TestProjectPaths(unittest.TestCase):
    def test_find_repo_root_default_no_args(self):
        repo_root = find_repo_root()
        self.assertTrue((repo_root / "package.json").is_file())
        self.assertTrue((repo_root / "README.md").is_file())

    def test_find_repo_root_from_file_path(self):
        file_path = Path(__file__).resolve()
        repo_root = find_repo_root(file_path)
        self.assertTrue((repo_root / "package.json").is_file())
        self.assertTrue((repo_root / "README.md").is_file())

    def test_find_repo_root_from_directory_path(self):
        dir_path = Path(__file__).resolve().parent
        repo_root = find_repo_root(dir_path)
        self.assertTrue((repo_root / "package.json").is_file())
        self.assertTrue((repo_root / "README.md").is_file())

    def test_find_repo_root_from_string_path(self):
        file_path_str = str(Path(__file__).resolve())
        repo_root = find_repo_root(file_path_str)
        self.assertTrue((repo_root / "package.json").is_file())

    def test_find_repo_root_raises_when_not_found(self):
        with tempfile.TemporaryDirectory() as tmp_dir:
            with self.assertRaises(FileNotFoundError):
                find_repo_root(tmp_dir)


if __name__ == "__main__":
    unittest.main()
