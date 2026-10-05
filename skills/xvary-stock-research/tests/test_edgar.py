import unittest
from unittest.mock import Mock, patch
from typing import Optional

from tools import edgar


class EdgarTests(unittest.TestCase):
    def test_shares_outstanding_does_not_include_weighted_average_concepts(self) -> None:
        concepts = edgar._FIELD_CONCEPTS["balance_sheet"]["shares_outstanding"]
        self.assertNotIn("WeightedAverageNumberOfDilutedSharesOutstanding", concepts)
        self.assertNotIn("WeightedAverageShares", concepts)

    def test_best_entry_uses_concept_priority_before_recency(self) -> None:
        records = [
            {
                "concept": "Revenue",
                "unit": "USD",
                "form": "10-K",
                "period_end": "2026-12-31",
                "filed": "2027-02-01",
                "period_months": 12,
            },
            {
                "concept": "Revenues",
                "unit": "USD",
                "form": "10-K",
                "period_end": "2025-12-31",
                "filed": "2026-02-01",
                "period_months": 12,
            },
        ]
        best = edgar._best_entry(
            records,
            quarterly=False,
            statement="income_statement",
            field="revenue",
        )
        self.assertIsNotNone(best)
        assert best is not None
        self.assertEqual(best["concept"], "Revenues")

    def test_request_json_retries_then_succeeds(self) -> None:
        class FakeResponse:
            def __init__(self, status_code: int, payload: Optional[dict] = None) -> None:
                self.status_code = status_code
                self._payload = payload or {}

            def raise_for_status(self) -> None:
                if self.status_code >= 400:
                    raise edgar.requests.HTTPError(response=self)

            def json(self) -> dict:
                return self._payload

        session = Mock()
        session.get.side_effect = [
            FakeResponse(503),
            FakeResponse(200, {"ok": True}),
        ]

        with patch("tools.edgar.time.sleep") as sleep_mock:
            data = edgar._request_json("https://example.com", session)

        self.assertEqual(data, {"ok": True})
        self.assertEqual(session.get.call_count, 2)
        sleep_mock.assert_called_once()

    def test_request_json_raises_after_max_retries(self) -> None:
        class FakeResponse:
            def __init__(self, status_code: int) -> None:
                self.status_code = status_code

            def raise_for_status(self) -> None:
                raise edgar.requests.HTTPError(response=self)

            def json(self) -> dict:
                return {}

        session = Mock()
        session.get.return_value = FakeResponse(503)

        with patch("tools.edgar.time.sleep"):
            with self.assertRaises(edgar.requests.HTTPError):
                edgar._request_json("https://example.com", session)
        self.assertEqual(session.get.call_count, edgar._MAX_RETRIES)

    @patch("tools.edgar._request_json")
    def test_get_cik_success_and_formatting(self, mock_request_json: Mock) -> None:
        mock_request_json.return_value = {
            "0": {"ticker": "AAPL", "cik_str": 320193},
            "1": {"ticker": "MSFT", "cik_str": 789019},
        }
        self.assertEqual(edgar.get_cik("aapl"), "0000320193")
        self.assertEqual(edgar.get_cik("MSFT"), "0000789019")

    @patch("tools.edgar._request_json")
    def test_get_cik_ticker_variants(self, mock_request_json: Mock) -> None:
        mock_request_json.return_value = {
            "0": {"ticker": "BRK.B", "cik_str": 1067983},
        }
        self.assertEqual(edgar.get_cik("BRK-B"), "0001067983")

    @patch("tools.edgar._request_json")
    def test_get_cik_not_found(self, mock_request_json: Mock) -> None:
        mock_request_json.return_value = {
            "0": {"ticker": "AAPL", "cik_str": 320193},
        }
        self.assertIsNone(edgar.get_cik("NONEXISTENT"))

    @patch("tools.edgar._request_json")
    def test_get_cik_handles_malformed_lookup_entries(self, mock_request_json: Mock) -> None:
        mock_request_json.return_value = {
            "0": "invalid_entry_not_a_dict",
            "1": {"ticker": "", "cik_str": 123},
            "2": {"ticker": "NVDA"},
            "3": {"ticker": "GOOGL", "cik_str": 1652044},
        }
        self.assertEqual(edgar.get_cik("GOOGL"), "0001652044")
        self.assertIsNone(edgar.get_cik("NVDA"))


if __name__ == "__main__":
    unittest.main()
