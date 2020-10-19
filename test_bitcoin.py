import unittest
from unittest import TestCase
from unittest.mock import patch
import bitcoin


class TestBitcoins(TestCase):
    bitcoins = 100
    exchange_rate = 11763.1797
    fake_response = {
        "time": {
            "updatedISO": "2020-10-19T16:55:00+00:00",
            "updated": "Oct 19, 2020 16:55:00 UTC",
            "updateduk": "Oct 19, 2020 at 17:55 BST"
        },
        "chartName": "Bitcoin",
        "disclaimer": "This data was produced from the CoinDesk Bitcoin Price Index (USD). Non-USD currency data converted using hourly conversion rate from openexchangerates.org",
        "bpi": {
            "EUR": {
                "rate": "9,979.0347",
                "symbol": "&euro;",
                "code": "EUR",
                "description": "Euro",
                "rate_float": 9979.0347
            },
            "GBP": {
                "description": "British Pound Sterling",
                "rate_float": 9051.1786,
                "symbol": "&pound;",
                "code": "GBP",
                "rate": "9,051.1786"
            },
            "USD": {
                "rate": str(exchange_rate),
                "symbol": "&#36;",
                "code": "USD",
                "description": "United States Dollar",
                "rate_float": exchange_rate
            }
        }
    }

    @patch("bitcoin.get_exchange_rate", side_effect=[fake_response])
    def test_get_exchange_rate(self, mock_service_call):
        value = bitcoin.get_exchange_rate()
        self.assertEqual(value, self.fake_response)

    def test_get_dollar_rate(self):
        rate = bitcoin.get_dollar_rate(self.fake_response)
        self.assertEqual(rate, self.exchange_rate)

    @patch("builtins.input", side_effect=['f', '20'])
    def test_get_users_bitcoins(self, mock_input):
        users_bitcoins = bitcoin.get_users_bitcoins()
        self.assertEqual(users_bitcoins, 20.0)

    def test_calculate_bitcoins_in_dollars(self):
        value_in_dollars = bitcoin.calculate_bitcoins_in_dollars(
            self.bitcoins, self.exchange_rate)
        self.assertEqual(value_in_dollars, self.bitcoins * self.exchange_rate)

    def test_format_exchange_statement(self):
        value_in_dollars = 1333.333
        correct_statement = "$100 Bitcoin is equivelent to $1333.333 in dollars"
        formatted_statement = bitcoin.format_exchange_statement(
            self.bitcoins, value_in_dollars)
        self.assertEqual(correct_statement, formatted_statement)


if __name__ == "__main__":
    unittest.main()
