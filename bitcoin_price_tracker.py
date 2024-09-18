import requests
import time
from datetime import datetime

def get_crypto_price(symbol):
    url = f'https://api.coingecko.com/api/v3/simple/price?ids={symbol}&vs_currencies=USD'
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()
        if symbol in data and 'usd' in data[symbol]:
            current_price = data[symbol]['usd']
            updated_at = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            return current_price, updated_at
        else:
            return None, None
    except requests.exceptions.HTTPError:
        if response.status_code == 429:
            print("Rate limit exceeded. Retrying in 60 seconds...")
            time.sleep(60)
            return get_crypto_price(symbol)
        return None, None
    except requests.exceptions.RequestException as err:
        print(f"Error fetching price data: {err}")
        return None, None

def get_historical_data(symbol, days):
    url = f'https://api.coingecko.com/api/v3/coins/{symbol}/market_chart?vs_currency=usd&days={days}'
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()
        historical_prices = data['prices']
        if historical_prices:
            last_update_timestamp = historical_prices[-1][0]
            last_update_date = datetime.fromtimestamp(last_update_timestamp / 1000).strftime('%Y-%m-%d %H:%M:%S')
            return historical_prices, last_update_date
        else:
            return None, None
    except requests.exceptions.HTTPError:
        if response.status_code == 429:
            print("Rate limit exceeded. Retrying in 60 seconds...")
            time.sleep(60)
            return get_historical_data(symbol, days)
        return None, None
    except requests.exceptions.RequestException as err:
        print(f"Error fetching historical data: {err}")
        return None, None

def calculate_average(prices):
    total_price = sum(price for _, price in prices)
    return total_price / len(prices)

def main():
    symbol = 'bitcoin'
    days = 30

    current_price, updated_at = get_crypto_price(symbol)
    if current_price is not None:
        print(f"Current BTC price: ${current_price} (Last updated: {updated_at})")

    historical_data, last_update_date = get_historical_data(symbol, days)
    if historical_data:
        average_price = calculate_average(historical_data)
        print(f"Average BTC price over last {days} days: ${average_price:.2f} (Last update: {last_update_date})")

if __name__ == "__main__":
    main()
