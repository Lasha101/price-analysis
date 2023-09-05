import random
import requests
import sys


# Convert the input date into a float value
def date(date):
    try:
        date = float(date)
        date = 12 - date
        return date
    except ValueError:
        raise ValueError("Only Integer or Float!")
    
def bitcoin_prices():
    prices = []
    url = 'https://api.coindesk.com/v1/bpi/currentprice.json'
    try:
        response = requests.get(url)
        data = response.json()
        string_price = float(data['bpi']['USD']['rate_float'])
        price = string_price
        price = price / 1000

        # Generate random fluctuations for 10 iterations
        for _ in range(12):
            price = round(price * random.uniform(0.1, 2))
            prices.append(price)
    except requests.RequestException:
        sys.exit()
    return prices