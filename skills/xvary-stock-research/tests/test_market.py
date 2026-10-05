import unittest
from unittest.mock import patch
from typing import Optional

from tools import market


class MarketTests(unittest.TestCase):
    def test_get_ratios_short_circuits_after_first_provider_with_ratios(self) -> None:
        calls: list[str] = []

        def yahoo(_ticker: str):
            calls.append("yahoo")
            return {
                "provider": "yahoo",
                "price": 100.0,
                "pe": 25.0,
                "dividend_yield_pct": 1.2,
                "beta": 1.1,
            }

        def finviz(_ticker: str):
            calls.append("finviz")
            return {
                "provider": "finviz",
                "price": 100.0,
                "pe": 18.0,
                "dividend_yield_pct": 2.0,
                "beta": 0.9,
            }

        def stooq(_ticker: str):
            calls.append("stooq")
            return {
                "provider": "stooq",
                "price": 100.0,
                "pe": None,
                "dividend_yield_pct": None,
                "beta": None,
            }

        with patch("tools.market._fetch_yahoo", yahoo), patch(
            "tools.market._fetch_finviz", finviz
        ), patch("tools.market._fetch_stooq", stooq):
            result = market.get_ratios("AAPL")

        self.assertEqual(result["provider"], "yahoo")
        self.assertEqual(calls, ["yahoo"])

    def test_get_ratios_uses_second_provider_when_first_has_no_ratios(self) -> None:
        calls: list[str] = []

        def yahoo(_ticker: str):
            calls.append("yahoo")
            return {
                "provider": "yahoo",
                "price": 100.0,
                "pe": None,
                "dividend_yield_pct": None,
                "beta": None,
            }

        def finviz(_ticker: str):
            calls.append("finviz")
            return {
                "provider": "finviz",
                "price": 100.0,
                "pe": 18.0,
                "dividend_yield_pct": 2.0,
                "beta": 0.9,
            }

        def stooq(_ticker: str):
            calls.append("stooq")
            return None

        with patch("tools.market._fetch_yahoo", yahoo), patch(
            "tools.market._fetch_finviz", finviz
        ), patch("tools.market._fetch_stooq", stooq):
            result = market.get_ratios("AAPL")

        self.assertEqual(result["provider"], "finviz")
        self.assertEqual(calls, ["yahoo", "finviz"])

    def test_get_quote_success(self) -> None:
        fake_data = {
            "provider": "yahoo",
            "price": 150.0,
            "currency": "USD",
            "market_cap": 2500000000000.0,
            "volume": 50000000.0,
            "high_52w": 180.0,
            "low_52w": 120.0,
        }
        with patch("tools.market._collect_market_data", return_value=fake_data) as mock_collect:
            quote = market.get_quote("  aapl  ")

        mock_collect.assert_called_once_with("AAPL")
        self.assertEqual(quote["ticker"], "AAPL")
        self.assertEqual(quote["provider"], "yahoo")
        self.assertEqual(quote["price"], 150.0)
        self.assertEqual(quote["currency"], "USD")
        self.assertEqual(quote["market_cap"], 2500000000000.0)
        self.assertEqual(quote["volume"], 50000000.0)
        self.assertEqual(quote["high_52w"], 180.0)
        self.assertEqual(quote["low_52w"], 120.0)
        self.assertIn("as_of_utc", quote)

    def test_get_quote_default_currency(self) -> None:
        fake_data = {
            "provider": "finviz",
            "price": 200.0,
        }
        with patch("tools.market._collect_market_data", return_value=fake_data):
            quote = market.get_quote("MSFT")

        self.assertEqual(quote["currency"], "USD")

    def test_get_quote_no_data_raises_runtime_error(self) -> None:
        with patch("tools.market._collect_market_data", return_value=None):
            with self.assertRaises(RuntimeError) as ctx:
                market.get_quote("UNKNOWN")

        self.assertIn("No quote data available for UNKNOWN", str(ctx.exception))

    def test_http_get_json_retries_then_succeeds(self) -> None:
        class FakeResponse:
            def __init__(self, status_code: int, payload: Optional[dict] = None) -> None:
                self.status_code = status_code
                self._payload = payload or {}

            def raise_for_status(self) -> None:
                if self.status_code >= 400:
                    raise market.requests.HTTPError(response=self)

            def json(self) -> dict:
                return self._payload

        with patch("tools.market.requests.get") as get_mock, patch(
            "tools.market.time.sleep"
        ) as sleep_mock:
            get_mock.side_effect = [
                FakeResponse(503),
                FakeResponse(200, {"ok": True}),
            ]
            payload = market._http_get_json("https://example.com")

        self.assertEqual(payload, {"ok": True})
        self.assertEqual(get_mock.call_count, 2)
        sleep_mock.assert_called_once()


if __name__ == "__main__":
    unittest.main()
