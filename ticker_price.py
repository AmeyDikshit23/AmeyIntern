from dotenv import load_dotenv
import os
import requests
from datetime import datetime

load_dotenv()  # Load variables from .env

api_key = os.getenv("API_KEY")

class PriceChangeAgent:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://api.example.com/stock"  # Replace with real API URL

    def get_stock_price(self, ticker, date):
        date_str = date.strftime("%Y-%m-%d")
        url = f"{self.base_url}/{ticker}/price?date={date_str}&apikey={self.api_key}"
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        return data['close']

    def calculate_price_change(self, ticker, start_date, end_date):
        start_price = self.get_stock_price(ticker, start_date)
        end_price = self.get_stock_price(ticker, end_date)
        change = ((end_price - start_price) / start_price) * 100
        return change

if __name__ == "__main__":
    agent = PriceChangeAgent(api_key)
    start = datetime(2023, 4, 1)
    end = datetime(2023, 5, 1)
    change = agent.calculate_price_change("AAPL", start, end)
    print(f"Price change for AAPL between {start.date()} and {end.date()}: {change:.2f}%")