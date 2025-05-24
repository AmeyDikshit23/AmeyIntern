import os
from dotenv import load_dotenv
from agents.ticker_news import TickerNewsAgent

load_dotenv()
NEWS_API_KEY = os.getenv("NEWS_API_KEY")

if not NEWS_API_KEY:
    raise Exception("Please set NEWS_API_KEY in your environment variables or .env file")

class TickerAnalysisAgent:
    def __init__(self):
        self.news_agent = TickerNewsAgent(NEWS_API_KEY)

    def analyze(self, ticker: str, company_name: str):
        news = self.news_agent.get_news(ticker, company_name)

        analysis_summary = f"Recent news for {company_name} ({ticker}):\n"
        for title, url in news:
            analysis_summary += f"- {title}\n  Link: {url}\n"

        return analysis_summary

if __name__ == "__main__":
    agent = TickerAnalysisAgent()
    result = agent.analyze("TSLA", "Tesla")
    print(result)
