from google_adk import Agent, Response
import os
import requests
from dotenv import load_dotenv

load_dotenv()
NEWS_API_KEY = os.getenv("NEWS_API_KEY")

class TickerNewsAgent(Agent):
    def __init__(self):
        super().__init__()
        self.api_key = NEWS_API_KEY
        self.base_url = "https://newsapi.org/v2/everything"

    def get_news(self, ticker, company_name):
        query = f"{company_name} OR {ticker}"
        params = {
            "q": query,
            "sortBy": "publishedAt",
            "apiKey": self.api_key,
            "pageSize": 5,
            "language": "en"
        }
        response = requests.get(self.base_url, params=params)
        data = response.json()
        articles = data.get("articles", [])
        return [(a["title"], a["url"]) for a in articles]

    async def handle(self, request):
        ticker = request.get("ticker")
        company_name = request.get("company_name")
        news = self.get_news(ticker, company_name)
        text = "\n".join(f"{title}\n{url}" for title, url in news)
        return Response(text=text)
