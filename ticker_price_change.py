import os
from dotenv import load_dotenv
import requests
from datetime import datetime

load_dotenv()  # Load API_KEY from .env file
api_key = os.getenv("API_KEY")

class PriceChangeAgent:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://www.alphavantage.co/query"

    def get_stock_price(self, ticker, date):
        date_str = date.strftime("%Y-%m-%d")
        params = {
            "function": "TIME_SERIES_DAILY_ADJUSTED",
            "symbol": ticker,
            "apikey": self.api_key,
            "outputsize": "full"
        }

        response = requests.get(self.base_url, params=params)
        response.raise_for_status()
        data = response.json()

        try:
            return float(data["Time Series (Daily)"][date_str]["4. close"])
        except KeyError:
            raise Exception(f"No price data available for {date_str}")

    def calculate_price_change(self, ticker, start_date, end_date):
        start_price = self.get_stock_price(ticker, start_date)
        end_price = self.get_stock_price(ticker, end_date)
        change = ((end_price - start_price) / start_price) * 100
        return change

if __name__ == "__main__":
    from datetime import timedelta

    agent = PriceChangeAgent(api_key)

    # Start checking from today and go backwards to find valid trading days
    today = datetime.now()
    end_date = today
    start_date = today - timedelta(days=5)

    try:
        # Try getting end date price
        while True:
            try:
                end_price = agent.get_stock_price("AAPL", end_date)
                break
            except Exception:
                end_date -= timedelta(days=1)

        # Try getting start date price
        while True:
            try:
                start_price = agent.get_stock_price("AAPL", start_date)
                break
            except Exception:
                start_date -= timedelta(days=1)

        change = ((end_price - start_price) / start_price) * 100
        print(f"Price change for AAPL between {start_date.date()} and {end_date.date()}: {change:.2f}%")

    except Exception as e:
        print("Error:", e)
