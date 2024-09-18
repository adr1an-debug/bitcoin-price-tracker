# Bitcoin Price Tracker

A Python script to fetch the current Bitcoin price and calculate the average price over the last 30 days using the CoinGecko API.

## Requirements

- **Python 3.6+**
- **Requests library**: Install with `pip install requests`

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/bitcoin-price-tracker.git
   cd bitcoin-price-tracker

2. Install dependencies:
`pip install requests`

3. Run the script:
`python bitcoin_price_tracker.py`

## Notes
- The script handles API rate limits and will retry after a 60-second delay if limits are exceeded.
- Adjust the `symbol` and `days` variables to track different cryptocurrencies or time periods.

## License
MIT License
