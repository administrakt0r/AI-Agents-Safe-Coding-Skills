"""
Tests for type_coverage.py

Run with: pytest skills/lint-and-validate/scripts/tests/test_type_coverage.py
"""

import sys
import pytest
from pathlib import Path
from unittest.mock import patch, MagicMock

sys.path.insert(0, str(Path(__file__).parent.parent))

from type_coverage import check_typescript_coverage, check_python_coverage, main


class TestTypeScriptCoverage:
    """Tests for check_typescript_coverage function."""

    def test_no_ts_files(self, tmp_path):
        """Test when no TypeScript files are present."""
        res = check_typescript_coverage(tmp_path)
        assert res['type'] == 'typescript'
        assert res['files'] == 0
        assert "[!] No TypeScript files found" in res['issues']
        assert res['stats']['any_count'] == 0

    def test_clean_typescript_files(self, tmp_path):
        """Test clean TypeScript files with high coverage and no 'any' types."""
        ts_file = tmp_path / "app.ts"
        ts_file.write_text("""
function add(a: number, b: number): number {
    return a + b;
}
const greet = (name: string): string => "Hello " + name;
""")

        res = check_typescript_coverage(tmp_path)
        assert res['files'] == 1
        assert any("[OK] No 'any' types found" in item for item in res['passed'])
        assert any("[OK] Type coverage: 100%" in item for item in res['passed'])
        assert res['stats']['any_count'] == 0

    def test_acceptable_any_and_warning_coverage(self, tmp_path):
        """Test acceptable 'any' count (<=5) and warning level coverage (50-79%)."""
        ts_file = tmp_path / "app.tsx"
        ts_file.write_text("""
const x: any = 10;
function untypedFunc(x, y) {
    return x + y;
}
function typedFunc(a: number): number {
    return a;
}
""")

        res = check_typescript_coverage(tmp_path)
        assert res['files'] == 1
        assert any("[!] 1 'any' types found (acceptable)" in item for item in res['issues'])
        assert any("[!] Type coverage: 50%" in item for item in res['issues'])

    def test_too_many_any_and_low_coverage(self, tmp_path):
        """Test too many 'any' types (>5) and critical low coverage (<50%)."""
        ts_file = tmp_path / "app.ts"
        # 6 'any' occurrences and 2 untyped functions, 0 typed functions
        ts_file.write_text("""
let a: any = 1;
let b: any = 2;
let c: any = 3;
let d: any = 4;
let e: any = 5;
let f: any = 6;
function f1(x) { return x; }
function f2(y) { return y; }
""")

        res = check_typescript_coverage(tmp_path)
        assert res['files'] == 1
        assert any("[X] 6 'any' types found (too many)" in item for item in res['issues'])
        assert any("[X] Type coverage: 0%" in item for item in res['issues'])

    def test_ignores_node_modules_and_d_ts(self, tmp_path):
        """Test that node_modules and .d.ts files are excluded."""
        node_mod = tmp_path / "node_modules" / "lib.ts"
        node_mod.parent.mkdir(parents=True)
        node_mod.write_text("function bad(x) {}")

        d_ts = tmp_path / "types.d.ts"
        d_ts.write_text("function decl(x);")

        res = check_typescript_coverage(tmp_path)
        assert res['files'] == 0
        assert "[!] No TypeScript files found" in res['issues']

    def test_file_read_exception_handled(self, tmp_path):
        """Test file read exception is safely handled."""
        ts_file = tmp_path / "unreadable.ts"
        ts_file.write_text("function test() {}")

        with patch.object(Path, 'read_text', side_effect=PermissionError("Denied")):
            res = check_typescript_coverage(tmp_path)
            assert res['files'] == 1
            assert res['stats']['total_functions'] == 0


class TestPythonCoverage:
    """Tests for check_python_coverage function."""

    def test_no_python_files(self, tmp_path):
        """Test when no Python files are present."""
        res = check_python_coverage(tmp_path)
        assert res['type'] == 'python'
        assert res['files'] == 0
        assert "[!] No Python files found" in res['issues']

    def test_python_coverage_high_and_clean(self, tmp_path):
        """Test Python files with high typed ratio and no Any types."""
        py_file = tmp_path / "script.py"
        py_file.write_text("""
def add(a: int, b: int):
    return a + b
def greet() -> str:
    return "Hello"
""")

        res = check_python_coverage(tmp_path)
        assert res['files'] == 1
        assert any("[OK] Type hints coverage: 100%" in item for item in res['passed'])
        assert any("[OK] No 'Any' types found" in item for item in res['passed'])

    def test_python_coverage_warning_and_acceptable_any(self, tmp_path):
        """Test Python file with medium coverage (40-69%) and acceptable Any (1-3)."""
        py_file = tmp_path / "script.py"
        py_file.write_text("""
val: Any = 1
def typed_func(a: int):
    pass
def untyped_func(b):
    pass
""")

        res = check_python_coverage(tmp_path)
        assert res['files'] == 1
        assert any("[!] Type hints coverage: 50%" in item for item in res['issues'])
        assert any("[!] 1 'Any' types found" in item for item in res['issues'])

    def test_python_coverage_low_and_high_any(self, tmp_path):
        """Test Python file with low coverage (<40%) and high Any (>3)."""
        py_file = tmp_path / "script.py"
        py_file.write_text("""
v1: Any = 1
v2: Any = 2
v3: Any = 3
v4: Any = 4
def u1(x): pass
def u2(y): pass
def u3(z): pass
""")

        res = check_python_coverage(tmp_path)
        assert res['files'] == 1
        assert any("[X] Type hints coverage: 0% (add type hints)" in item for item in res['issues'])
        assert any("[X] 4 'Any' types found" in item for item in res['issues'])

    def test_python_excludes_venv_and_cache(self, tmp_path):
        """Test that venv and __pycache__ files are ignored."""
        venv_py = tmp_path / "venv" / "lib.py"
        venv_py.parent.mkdir(parents=True)
        venv_py.write_text("def f(): pass")

        cache_py = tmp_path / "__pycache__" / "cached.py"
        cache_py.parent.mkdir(parents=True)
        cache_py.write_text("def f(): pass")

        res = check_python_coverage(tmp_path)
        assert res['files'] == 0

    def test_python_read_exception_handled(self, tmp_path):
        """Test read exception handling for Python files."""
        py_file = tmp_path / "broken.py"
        py_file.write_text("def foo(): pass")

        with patch.object(Path, 'read_text', side_effect=OSError("Read error")):
            res = check_python_coverage(tmp_path)
            assert res['files'] == 1
            assert res['stats']['typed_functions'] == 0


class TestMainCLI:
    """Tests for main CLI entrypoint."""

    def test_main_no_files_found(self, tmp_path):
        """Test main when no TS or Python files are found."""
        with patch('sys.argv', ['type_coverage.py', str(tmp_path)]):
            with pytest.raises(SystemExit) as exc:
                main()
            assert exc.value.code == 0

    def test_main_success_clean_project(self, tmp_path):
        """Test main when all checks pass with clean files."""
        py_file = tmp_path / "main.py"
        py_file.write_text("def run(val: int) -> None:\n    pass\n")

        with patch('sys.argv', ['type_coverage.py', str(tmp_path)]):
            with pytest.raises(SystemExit) as exc:
                main()
            assert exc.value.code == 0

    def test_main_failure_critical_issues(self, tmp_path):
        """Test main when critical issues exist."""
        ts_file = tmp_path / "bad.ts"
        ts_file.write_text("""
let a: any = 1;
let b: any = 2;
let c: any = 3;
let d: any = 4;
let e: any = 5;
let f: any = 6;
""")

        with patch('sys.argv', ['type_coverage.py', str(tmp_path)]):
            with pytest.raises(SystemExit) as exc:
                main()
            assert exc.value.code == 1
