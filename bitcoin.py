import requests

def get_exchange_rate():
    url = "https://api.coindesk.com/v1/bpi/currentprice.json"
    response =  requests.get(url)
    return response.json()

def get_dollar_rate(data):
    return data["bpi"]["USD"]["rate_float"]

def get_users_bitcoins():
    while True:
        try:
            bitcoins = float(input("Enter number of Bitcoins: "))
            return bitcoins
        except ValueError:
            print('please enter a number')

def calculate_bitcoins_in_dollars(bitcoins, exchange_rate):
    return bitcoins * exchange_rate

def format_exchange_statement(bitcoin, bitcoin_value_in_dollars):
    return f"${bitcoin} Bitcoin is equivelent to ${bitcoin_value_in_dollars} in dollars"

response = get_exchange_rate()
exchange_rate = get_dollar_rate(response)
user_bitcoins = get_users_bitcoins()
value_in_dollars = calculate_bitcoins_in_dollars(user_bitcoins, exchange_rate)
exchange_statement = format_exchange_statement(user_bitcoins, value_in_dollars)
print(exchange_statement)