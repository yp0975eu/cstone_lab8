from unittest import TestCase
import bitcoin

class TestBitcoins(TestCase):
    def test_get_exchange_rate(self):
        pass

    def test_get_dollar_rate(self):
        rate = 100
        fake_response = {
            "bpi": {
                "USD": {
                    "rate_float": rate
                }
            }
        }
        exchange_rate = bitcoin.get_dollar_rate(fake_response)
        self.assertEqual(rate, exchange_rate)

    def test_get_users_bitcoins(self):
        pass

    def test_calculate_bitcoins_in_dollars(self):
        bitcoins = 100
        exchange_rate = 1333.333

        value_in_dollars = bitcoin.calculate_bitcoins_in_dollars(bitcoins, exchange_rate)
        self.assertEqual(value_in_dollars, bitcoins * exchange_rate)

    def test_format_exchange_statement(self):
        bitcoins = 100
        value_in_dollars = 1333.333
        correct_statement = "$100 Bitcoin is equivelent to $1333.333 in dollars"
        formatted_statement = bitcoin.format_exchange_statement(bitcoins, value_in_dollars)
        self.assertEqual(correct_statement, formatted_statement)