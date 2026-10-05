import sys
import time
import unittest
from unittest.mock import patch, MagicMock
from pathlib import Path

# Add script directory to sys.path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))

import sync_to_notion


class TestNotionBlockDeletion(unittest.TestCase):

    @patch("sync_to_notion.requests.delete")
    @patch("sync_to_notion.notion_request")
    def test_update_business_section_deletion_performance(self, mock_notion_request, mock_requests_delete):
        # Setup mock responses
        # notion_request("patch", ...) for page metadata
        # notion_request("get", ...) for blocks listing
        all_blocks = [
            {"id": "h2_business", "type": "heading_2", "heading_2": {"rich_text": [{"plain_text": "💼 Business"}]}}
        ]
        # Add 20 blocks to delete in Business section
        for i in range(20):
            all_blocks.append({"id": f"block_{i}", "type": "paragraph"})
        all_blocks.append({"id": "h2_next", "type": "heading_2", "heading_2": {"rich_text": [{"plain_text": "Next Section"}]}})

        def side_effect_notion_request(method, endpoint, data=None):
            if method == "get" and "children" in endpoint:
                return {"results": all_blocks, "has_more": False}
            return {}

        mock_notion_request.side_effect = side_effect_notion_request

        # Simulate 50ms latency per HTTP DELETE call
        def delayed_delete(url, headers=None):
            time.sleep(0.05)
            response = MagicMock()
            response.status_code = 200
            return response

        mock_requests_delete.side_effect = delayed_delete

        metadata = {
            "title": "Test Title",
            "projects": ["Test Project"],
            "tags": ["Business"],
        }
        business_blocks = [{"type": "paragraph", "paragraph": {"rich_text": []}}]

        start_time = time.time()
        sync_to_notion.update_business_section("test_page_id", metadata, business_blocks)
        elapsed_time = time.time() - start_time

        print(f"\n[BENCHMARK] Time taken for 20 block deletions: {elapsed_time:.4f} seconds")
        self.assertEqual(mock_requests_delete.call_count, 20)


if __name__ == "__main__":
    unittest.main()
