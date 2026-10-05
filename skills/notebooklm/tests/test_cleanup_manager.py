"""Tests for NotebookLM CleanupManager."""

import sys
import unittest
from pathlib import Path
from unittest.mock import MagicMock, patch

# Add scripts directory to sys.path
sys.path.insert(0, str(Path(__file__).parent.parent / "scripts"))

from cleanup_manager import CleanupManager


class TestCleanupManagerGetSize(unittest.TestCase):
    """Test _get_size method in CleanupManager including error paths."""

    def setUp(self):
        self.manager = CleanupManager()

    def test_get_size_nonexistent_path(self):
        """Test _get_size for a path that does not exist."""
        path = MagicMock(spec=Path)
        path.is_file.return_value = False
        path.is_dir.return_value = False
        self.assertEqual(self.manager._get_size(path), 0)

    def test_get_size_file(self):
        """Test _get_size for a regular file."""
        path = MagicMock(spec=Path)
        path.is_file.return_value = True
        path.is_dir.return_value = False
        path.stat.return_value.st_size = 1024

        self.assertEqual(self.manager._get_size(path), 1024)

    def test_get_size_directory_success(self):
        """Test _get_size for a directory with files."""
        dir_path = MagicMock(spec=Path)
        dir_path.is_file.return_value = False
        dir_path.is_dir.return_value = True

        item1 = MagicMock(spec=Path)
        item1.is_file.return_value = True
        item1.stat.return_value.st_size = 500

        item2 = MagicMock(spec=Path)
        item2.is_file.return_value = True
        item2.stat.return_value.st_size = 300

        dir_path.rglob.return_value = [item1, item2]

        self.assertEqual(self.manager._get_size(dir_path), 800)

    def test_get_size_directory_exception(self):
        """Test _get_size graceful error handling when rglob raises an Exception."""
        dir_path = MagicMock(spec=Path)
        dir_path.is_file.return_value = False
        dir_path.is_dir.return_value = True
        dir_path.rglob.side_effect = PermissionError("Permission denied")

        # Must return 0 without raising an exception when rglob fails
        self.assertEqual(self.manager._get_size(dir_path), 0)

    def test_get_size_directory_stat_exception(self):
        """Test _get_size graceful error handling when stat() on an item inside rglob raises an Exception."""
        dir_path = MagicMock(spec=Path)
        dir_path.is_file.return_value = False
        dir_path.is_dir.return_value = True

        item_err = MagicMock(spec=Path)
        item_err.is_file.return_value = True
        item_err.stat.side_effect = OSError("Access denied")

        dir_path.rglob.return_value = [item_err]

        self.assertEqual(self.manager._get_size(dir_path), 0)


class TestCleanupManagerFormatSize(unittest.TestCase):
    """Test _format_size formatting utility."""

    def setUp(self):
        self.manager = CleanupManager()

    def test_format_size_bytes(self):
        self.assertEqual(self.manager._format_size(500), "500.0 B")

    def test_format_size_kilobytes(self):
        self.assertEqual(self.manager._format_size(2048), "2.0 KB")

    def test_format_size_megabytes(self):
        self.assertEqual(self.manager._format_size(1048576 * 5), "5.0 MB")


class TestCleanupManagerPerformCleanup(unittest.TestCase):
    """Test perform_cleanup including failure handling."""

    def setUp(self):
        self.manager = CleanupManager()

    @patch.object(CleanupManager, 'get_cleanup_paths')
    def test_perform_cleanup_dry_run(self, mock_get_paths):
        mock_get_paths.return_value = {
            'total_items': 3,
            'total_size': 1000,
            'categories': {}
        }
        res = self.manager.perform_cleanup(dry_run=True)
        self.assertTrue(res['dry_run'])
        self.assertEqual(res['would_delete'], 3)
        self.assertEqual(res['would_free'], 1000)

    @patch.object(CleanupManager, 'get_cleanup_paths')
    @patch('cleanup_manager.Path')
    def test_perform_cleanup_handles_deletion_failure(self, mock_path_cls, mock_get_paths):
        mock_get_paths.return_value = {
            'categories': {
                'other': [{'path': '/dummy/file.txt', 'size': 100}]
            }
        }
        mock_target = MagicMock()
        mock_target.exists.return_value = True
        mock_target.is_dir.return_value = False
        mock_target.unlink.side_effect = PermissionError("Permission denied")
        mock_target.name = "file.txt"
        mock_target.__str__.return_value = '/dummy/file.txt'

        mock_path_cls.return_value = mock_target

        res = self.manager.perform_cleanup(dry_run=False)
        self.assertEqual(res['failed_count'], 1)
        self.assertEqual(res['deleted_count'], 0)
        self.assertEqual(res['failed_items'][0]['path'], '/dummy/file.txt')


if __name__ == "__main__":
    unittest.main()
