"""Tests for BaseWorker in templates/base_worker_template.py."""

import asyncio
import logging
import sys
import unittest
from pathlib import Path

# Add templates directory to sys.path
TEMPLATES_DIR = Path(__file__).resolve().parent.parent / "templates"
sys.path.insert(0, str(TEMPLATES_DIR))

from base_worker_template import BaseWorker, ExampleWorker


class FaultyWorker(BaseWorker):
    """Worker subclass that fails on specific items to test error handling."""

    def __init__(self, input_queue: asyncio.Queue, output_queue: asyncio.Queue):
        super().__init__(input_queue, output_queue)
        self.processed_items = []
        self.failed_items = []

    async def process(self, item: str):
        if item == "FAIL":
            self.failed_items.append(item)
            raise RuntimeError("Processing failed intentionally")
        self.processed_items.append(item)
        await self.output_queue.put(item.upper())


class TestBaseWorker(unittest.IsolatedAsyncioTestCase):

    async def test_error_path_logging_and_continuation(self):
        """Test that errors in process() are logged and the loop continues processing subsequent items."""
        input_q = asyncio.Queue()
        output_q = asyncio.Queue()
        worker = FaultyWorker(input_q, output_q)

        worker.start()

        # Enqueue item that causes exception followed by valid item
        await input_q.put("FAIL")
        await input_q.put("success")

        with self.assertLogs("base_worker_template", level="ERROR") as cm:
            # Wait until success item is processed into output queue
            res = await asyncio.wait_for(output_q.get(), timeout=2.0)

        self.assertEqual(res, "SUCCESS")
        self.assertEqual(worker.failed_items, ["FAIL"])
        self.assertEqual(worker.processed_items, ["success"])
        self.assertTrue(any("Error processing item: Processing failed intentionally" in log for log in cm.output))

        worker.terminate()
        await worker.wait_for_completion()

    async def test_happy_path_example_worker(self):
        """Test standard processing using ExampleWorker."""
        input_q = asyncio.Queue()
        output_q = asyncio.Queue()
        worker = ExampleWorker(input_q, output_q)

        worker.start()
        await input_q.put("hello")

        result = await asyncio.wait_for(output_q.get(), timeout=2.0)
        self.assertEqual(result, "HELLO")
        self.assertEqual(worker.processed_count, 1)

        worker.terminate()
        await worker.wait_for_completion()

    async def test_not_implemented_error(self):
        """Test that BaseWorker.process raises NotImplementedError."""
        input_q = asyncio.Queue()
        output_q = asyncio.Queue()
        worker = BaseWorker(input_q, output_q)

        with self.assertRaises(NotImplementedError):
            await worker.process("item")

    async def test_task_cancellation_during_shutdown(self):
        """Test worker cancellation when terminated while waiting on queue."""
        input_q = asyncio.Queue()
        output_q = asyncio.Queue()
        worker = ExampleWorker(input_q, output_q)

        worker.start()
        await asyncio.sleep(0.05)  # Let worker start and block on input_q.get()

        with self.assertLogs("base_worker_template", level="INFO") as cm:
            worker.terminate()
            await worker.wait_for_completion()

        self.assertFalse(worker.active)
        self.assertTrue(any("Task cancelled" in log for log in cm.output))


if __name__ == "__main__":
    unittest.main()
