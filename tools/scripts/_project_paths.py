"""Utility module for resolving repository paths across tooling scripts."""

from __future__ import annotations

from pathlib import Path

__all__ = ["find_repo_root"]


def find_repo_root(start_path: str | Path | None = None) -> Path:
    """Finds the root directory of the repository starting from a given path.

    Traverses up parent directories until finding a directory containing both
    'package.json' and 'README.md'. If start_path is omitted, starts searching
    from the current file's directory.
    """
    if start_path is None:
        start_path = Path(__file__).resolve().parent

    current = Path(start_path).resolve()
    if current.is_file():
        current = current.parent

    for candidate in (current, *current.parents):
        if (candidate / "package.json").is_file() and (candidate / "README.md").is_file():
            return candidate

    raise FileNotFoundError(f"Could not find repository root from {start_path!r}")
