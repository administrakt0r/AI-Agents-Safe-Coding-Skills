import sys
import json
import unittest
from pathlib import Path
import tempfile

# Add parent scripts directory to sys.path
SCRIPTS_DIR = Path(__file__).resolve().parent.parent / "scripts"
if str(SCRIPTS_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPTS_DIR))

from lint_runner import detect_project_type


class TestDetectProjectType(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.project_path = Path(self.temp_dir.name)

    def tearDown(self):
        self.temp_dir.cleanup()

    def test_detect_unknown_project(self):
        """Test detection when no recognizable project files exist."""
        res = detect_project_type(self.project_path)
        self.assertEqual(res["type"], "unknown")
        self.assertEqual(res["linters"], [])

    def test_detect_node_project_with_lint_script(self):
        """Test Node.js project detection with a lint script in package.json."""
        pkg_data = {
            "name": "test-node-project",
            "scripts": {
                "lint": "eslint ."
            }
        }
        (self.project_path / "package.json").write_text(json.dumps(pkg_data), encoding="utf-8")

        res = detect_project_type(self.project_path)
        self.assertEqual(res["type"], "node")
        self.assertEqual(len(res["linters"]), 1)
        self.assertEqual(res["linters"][0]["name"], "npm lint")
        self.assertEqual(res["linters"][0]["cmd"], ["npm", "run", "lint"])

    def test_detect_node_project_with_eslint_dep(self):
        """Test Node.js project detection with eslint dependency (and no lint script)."""
        pkg_data = {
            "devDependencies": {
                "eslint": "^8.0.0"
            }
        }
        (self.project_path / "package.json").write_text(json.dumps(pkg_data), encoding="utf-8")

        res = detect_project_type(self.project_path)
        self.assertEqual(res["type"], "node")
        self.assertEqual(len(res["linters"]), 1)
        self.assertEqual(res["linters"][0]["name"], "eslint")
        self.assertEqual(res["linters"][0]["cmd"], ["npx", "eslint", "."])

    def test_detect_node_project_with_typescript_dep(self):
        """Test Node.js project detection with typescript dependency."""
        pkg_data = {
            "devDependencies": {
                "typescript": "^5.0.0"
            }
        }
        (self.project_path / "package.json").write_text(json.dumps(pkg_data), encoding="utf-8")

        res = detect_project_type(self.project_path)
        self.assertEqual(res["type"], "node")
        self.assertEqual(len(res["linters"]), 1)
        self.assertEqual(res["linters"][0]["name"], "tsc")
        self.assertEqual(res["linters"][0]["cmd"], ["npx", "tsc", "--noEmit"])

    def test_detect_node_project_with_tsconfig(self):
        """Test Node.js project detection with tsconfig.json file present."""
        pkg_data = {"name": "test-ts"}
        (self.project_path / "package.json").write_text(json.dumps(pkg_data), encoding="utf-8")
        (self.project_path / "tsconfig.json").write_text("{}", encoding="utf-8")

        res = detect_project_type(self.project_path)
        self.assertEqual(res["type"], "node")
        self.assertEqual(len(res["linters"]), 1)
        self.assertEqual(res["linters"][0]["name"], "tsc")

    def test_detect_node_project_malformed_json(self):
        """Test Node.js project detection when package.json is invalid JSON."""
        (self.project_path / "package.json").write_text("{ invalid json ...", encoding="utf-8")

        res = detect_project_type(self.project_path)
        self.assertEqual(res["type"], "node")
        self.assertEqual(res["linters"], [])

    def test_detect_python_project_pyproject(self):
        """Test Python project detection with pyproject.toml."""
        (self.project_path / "pyproject.toml").write_text("[tool.poetry]\nname = 'test'", encoding="utf-8")

        res = detect_project_type(self.project_path)
        self.assertEqual(res["type"], "python")
        linter_names = [l["name"] for l in res["linters"]]
        self.assertIn("ruff", linter_names)
        self.assertIn("mypy", linter_names)

    def test_detect_python_project_requirements_only(self):
        """Test Python project detection with requirements.txt (no mypy config)."""
        (self.project_path / "requirements.txt").write_text("requests==2.28.0\n", encoding="utf-8")

        res = detect_project_type(self.project_path)
        self.assertEqual(res["type"], "python")
        linter_names = [l["name"] for l in res["linters"]]
        self.assertIn("ruff", linter_names)
        self.assertNotIn("mypy", linter_names)

    def test_detect_python_project_mypy_ini(self):
        """Test Python project detection with requirements.txt and mypy.ini."""
        (self.project_path / "requirements.txt").write_text("pytest\n", encoding="utf-8")
        (self.project_path / "mypy.ini").write_text("[mypy]\nignore_missing_imports = True\n", encoding="utf-8")

        res = detect_project_type(self.project_path)
        self.assertEqual(res["type"], "python")
        linter_names = [l["name"] for l in res["linters"]]
        self.assertIn("ruff", linter_names)
        self.assertIn("mypy", linter_names)

    def test_detect_hybrid_project(self):
        """Test detection when project contains both package.json and pyproject.toml."""
        pkg_data = {"scripts": {"lint": "eslint ."}}
        (self.project_path / "package.json").write_text(json.dumps(pkg_data), encoding="utf-8")
        (self.project_path / "pyproject.toml").write_text("[project]\nname = 'hybrid'", encoding="utf-8")

        res = detect_project_type(self.project_path)
        self.assertEqual(res["type"], "python")
        linter_names = [l["name"] for l in res["linters"]]
        self.assertIn("npm lint", linter_names)
        self.assertIn("ruff", linter_names)
        self.assertIn("mypy", linter_names)


if __name__ == "__main__":
    unittest.main()
