import json
import pytest
from unittest.mock import patch, mock_open
from pathlib import Path
import tempfile
import sys

# Ensure scripts directory is in python path
sys.path.insert(0, str(Path(__file__).parent.parent / "scripts"))

from notebook_manager import NotebookLibrary


@pytest.fixture
def temp_library_dir(tmp_path):
    """Fixture providing a temporary directory for notebook library tests."""
    data_dir = tmp_path / "data"
    data_dir.mkdir(parents=True, exist_ok=True)
    return tmp_path


def create_notebook_library_with_dir(temp_dir):
    """Helper to instantiate NotebookLibrary pointed to a temp directory."""
    with patch("notebook_manager.Path") as mock_path:
        # We replace the skill_dir computation so data_dir becomes temp_dir / "data"
        def path_side_effect(*args):
            if args and args[0] == __file__:
                # Simulate script path returning parent directory as temp_dir
                fake_script = temp_dir / "scripts" / "notebook_manager.py"
                return fake_script
            return Path(*args)

        mock_path.side_effect = path_side_effect
        # Re-import or patch internal Path for __file__ logic in __init__
        lib = NotebookLibrary()
        return lib


class TestNotebookLibraryErrorHandling:
    """Tests focusing on error handling paths in NotebookLibrary."""

    def test_load_library_corrupt_json(self, tmp_path):
        """Test _load_library when the library file contains invalid JSON."""
        data_dir = tmp_path / "data"
        data_dir.mkdir(parents=True, exist_ok=True)
        library_file = data_dir / "library.json"

        # Write invalid JSON to library_file
        library_file.write_text("{ corrupt json data: ", encoding="utf-8")

        with patch("notebook_manager.Path") as mock_path:
            mock_path.return_value.parent.parent = tmp_path
            lib = NotebookLibrary()

            # Verify that error handling was triggered and library state was reset safely
            assert lib.notebooks == {}
            assert lib.active_notebook_id is None

    def test_load_library_read_exception(self, tmp_path):
        """Test _load_library when reading the library file raises an Exception (e.g. PermissionError/IOError)."""
        data_dir = tmp_path / "data"
        data_dir.mkdir(parents=True, exist_ok=True)
        library_file = data_dir / "library.json"
        library_file.write_text("{}", encoding="utf-8")

        with patch("notebook_manager.Path") as mock_path:
            mock_path.return_value.parent.parent = tmp_path
            with patch("builtins.open", side_effect=PermissionError("Permission denied")):
                lib = NotebookLibrary()

                assert lib.notebooks == {}
                assert lib.active_notebook_id is None

    def test_save_library_exception(self, tmp_path):
        """Test _save_library error handling when writing to disk fails."""
        with patch("notebook_manager.Path") as mock_path:
            mock_path.return_value.parent.parent = tmp_path
            lib = NotebookLibrary()

            # Attempt to add notebook while builtins.open raises an error on save
            with patch("builtins.open", side_effect=OSError("Disk full or write error")):
                # _save_library should catch the exception and print error without crashing
                lib._save_library()


class TestNotebookLibraryOperations:
    """Tests covering standard NotebookLibrary CRUD operations and methods."""

    def test_initialization_creates_file_if_missing(self, tmp_path):
        """Test that missing library file triggers _save_library to create it."""
        with patch("notebook_manager.Path") as mock_path:
            mock_path.return_value.parent.parent = tmp_path
            lib = NotebookLibrary()

            library_file = tmp_path / "data" / "library.json"
            assert library_file.exists()
            assert lib.notebooks == {}
            assert lib.active_notebook_id is None

    def test_add_and_get_notebook(self, tmp_path):
        """Test adding notebooks and fetching them by ID."""
        with patch("notebook_manager.Path") as mock_path:
            mock_path.return_value.parent.parent = tmp_path
            lib = NotebookLibrary()

            notebook = lib.add_notebook(
                url="https://notebooklm.google.com/notebook/123",
                name="Test Notebook",
                description="A test notebook",
                topics=["Python", "Testing"],
                tags=["unit-test"]
            )

            assert notebook["id"] == "test-notebook"
            assert lib.active_notebook_id == "test-notebook"
            assert lib.get_notebook("test-notebook") == notebook

    def test_add_duplicate_notebook_raises_value_error(self, tmp_path):
        """Test that adding a duplicate notebook ID raises ValueError."""
        with patch("notebook_manager.Path") as mock_path:
            mock_path.return_value.parent.parent = tmp_path
            lib = NotebookLibrary()

            lib.add_notebook(
                url="https://notebooklm.google.com/notebook/123",
                name="Duplicate Test",
                description="First",
                topics=["Topic"]
            )

            with pytest.raises(ValueError, match="already exists"):
                lib.add_notebook(
                    url="https://notebooklm.google.com/notebook/456",
                    name="Duplicate Test",
                    description="Second",
                    topics=["Topic"]
                )

    def test_remove_notebook(self, tmp_path):
        """Test removing notebooks and active ID re-assignment."""
        with patch("notebook_manager.Path") as mock_path:
            mock_path.return_value.parent.parent = tmp_path
            lib = NotebookLibrary()

            nb1 = lib.add_notebook("https://url1", "NB One", "Desc 1", ["T1"])
            nb2 = lib.add_notebook("https://url2", "NB Two", "Desc 2", ["T2"])

            # nb1 was active because it was added first
            assert lib.active_notebook_id == "nb-one"

            # Remove active notebook nb1
            removed = lib.remove_notebook("nb-one")
            assert removed is True
            assert lib.get_notebook("nb-one") is None
            # active_notebook_id should switch to nb2
            assert lib.active_notebook_id == "nb-two"

            # Remove non-existent notebook
            assert lib.remove_notebook("non-existent") is False

            # Remove remaining notebook nb2
            lib.remove_notebook("nb-two")
            assert lib.active_notebook_id is None

    def test_update_notebook(self, tmp_path):
        """Test updating notebook fields."""
        with patch("notebook_manager.Path") as mock_path:
            mock_path.return_value.parent.parent = tmp_path
            lib = NotebookLibrary()

            lib.add_notebook("https://url", "Initial", "Desc", ["T1"])
            updated = lib.update_notebook(
                "initial",
                name="Updated Name",
                description="Updated Desc",
                topics=["T2"],
                content_types=["pdf"],
                use_cases=["study"],
                tags=["tag1"],
                url="https://new-url"
            )

            assert updated["name"] == "Updated Name"
            assert updated["description"] == "Updated Desc"
            assert updated["topics"] == ["T2"]
            assert updated["content_types"] == ["pdf"]
            assert updated["use_cases"] == ["study"]
            assert updated["tags"] == ["tag1"]
            assert updated["url"] == "https://new-url"

            with pytest.raises(ValueError, match="Notebook not found"):
                lib.update_notebook("missing-id", name="New Name")

    def test_search_and_list_notebooks(self, tmp_path):
        """Test listing and searching notebooks."""
        with patch("notebook_manager.Path") as mock_path:
            mock_path.return_value.parent.parent = tmp_path
            lib = NotebookLibrary()

            lib.add_notebook("https://url1", "Machine Learning", "ML guide", ["AI", "Python"], use_cases=["Research"])
            lib.add_notebook("https://url2", "Cooking Recipes", "Food items", ["Food"], tags=["kitchen"])

            all_nbs = lib.list_notebooks()
            assert len(all_nbs) == 2

            search_ml = lib.search_notebooks("Machine")
            assert len(search_ml) == 1
            assert search_ml[0]["id"] == "machine-learning"

            search_research = lib.search_notebooks("Research")
            assert len(search_research) == 1

            search_none = lib.search_notebooks("NonExistentKeyword")
            assert len(search_none) == 0

    def test_select_and_get_active_notebook(self, tmp_path):
        """Test selecting active notebook."""
        with patch("notebook_manager.Path") as mock_path:
            mock_path.return_value.parent.parent = tmp_path
            lib = NotebookLibrary()

            lib.add_notebook("https://url1", "NB 1", "Desc 1", ["T1"])
            lib.add_notebook("https://url2", "NB 2", "Desc 2", ["T2"])

            selected = lib.select_notebook("nb-2")
            assert selected["id"] == "nb-2"
            assert lib.get_active_notebook()["id"] == "nb-2"

            with pytest.raises(ValueError, match="Notebook not found"):
                lib.select_notebook("invalid-id")

    def test_increment_use_count_and_stats(self, tmp_path):
        """Test usage incrementing and stats aggregation."""
        with patch("notebook_manager.Path") as mock_path:
            mock_path.return_value.parent.parent = tmp_path
            lib = NotebookLibrary()

            lib.add_notebook("https://url1", "NB 1", "Desc 1", ["Topic A", "Topic B"])
            lib.add_notebook("https://url2", "NB 2", "Desc 2", ["Topic B", "Topic C"])

            lib.increment_use_count("nb-1")
            lib.increment_use_count("nb-1")
            lib.increment_use_count("nb-2")

            stats = lib.get_stats()
            assert stats["total_notebooks"] == 2
            assert stats["total_topics"] == 3
            assert stats["total_use_count"] == 3
            assert stats["most_used_notebook"]["id"] == "nb-1"

            with pytest.raises(ValueError, match="Notebook not found"):
                lib.increment_use_count("unknown")
