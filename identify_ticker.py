class IdentifyTickerAgent:
    def __init__(self):
        # Add more companies as needed
        self.company_to_ticker = {
            "tesla": "TSLA",
            "nvidia": "NVDA",
            "palantir": "PLTR",
            "apple": "AAPL",
            "microsoft": "MSFT",
            "google": "GOOGL",
            "meta": "META",
            "amazon": "AMZN"
        }

    def extract_ticker(self, user_query: str) -> str:
        query = user_query.lower()
        for name, ticker in self.company_to_ticker.items():
            if name in query:
                return ticker
        return None

_agent = IdentifyTickerAgent()

def identify_ticker(user_query: str) -> str:
    return _agent.extract_ticker(user_query)

if __name__ == "__main__":
    agent = IdentifyTickerAgent()
    test_queries = [
        "Why did Tesla stock drop today?",
        "What’s happening with Palantir stock?",
        "How has Nvidia changed in the last 7 days?"
    ]
    
    for q in test_queries:
        print(f"Query: {q} -> Ticker: {agent.extract_ticker(q)}")
