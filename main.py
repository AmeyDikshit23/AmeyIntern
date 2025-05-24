from dotenv import load_dotenv
import os

from agents.identify_ticker import IdentifyTickerAgent
from agents.ticker_price import PriceChangeAgent
from agents.ticker_price_change import PriceChangeAgent
from agents.ticker_news import TickerNewsAgent
from agents.ticker_analysis import TickerAnalysisAgent

def main():
    load_dotenv()  # Load API keys from .env

    # Get user input
    user_query = input("Enter your stock query: ")

    # Identify ticker from query
    identifier = IdentifyTickerAgent()
    ticker = identifier.extract_ticker(user_query)
    if not ticker:
        print("Sorry, could not identify the stock ticker.")
        return
    
    # Map ticker to company name (extend as needed)
    company_map = {
        "TSLA": "Tesla",
        "NVDA": "Nvidia",
        "PLTR": "Palantir",
        "AAPL": "Apple",
        "MSFT": "Microsoft",
        "GOOGL": "Google",
        "META": "Meta",
        "AMZN": "Amazon"
    }
    company_name = company_map.get(ticker, ticker)

    # Load API keys from environment variables
    STOCK_API_KEY = os.getenv("STOCK_API_KEY")
    NEWS_API_KEY = os.getenv("NEWS_API_KEY")

    if not STOCK_API_KEY or not NEWS_API_KEY:
        print("Missing required API keys. Please set STOCK_API_KEY and NEWS_API_KEY in your .env file.")
        return

    # Instantiate agents with API keys
    price_agent = TickerPriceAgent(STOCK_API_KEY)
    price_change_agent = TickerPriceChangeAgent(STOCK_API_KEY)
    news_agent = TickerNewsAgent(NEWS_API_KEY)
    analysis_agent = TickerAnalysisAgent(price_agent, price_change_agent, news_agent)

    # Run analysis
    analysis = analysis_agent.analyze(ticker, company_name)

    print("\n=== Analysis ===")
    print(analysis)

if __name__ == "__main__":
    main()

