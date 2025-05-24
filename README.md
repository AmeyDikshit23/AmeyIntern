# AmeyIntern
# 📈 Stock Market Multi-Agent System

This project is a simulation of a **multi-agent system** designed to analyze stock market sentiment and suggest simple trading decisions (BUY / SELL / HOLD). Each agent in the system is responsible for a specific task, enabling modular, extensible behavior.

---

## 🧠 Agents Overview

1. **TickerNewsAgent**  
   Fetches the latest news headlines related to a given stock ticker.

2. **SentimentAnalyzerAgent**  
   Analyzes the sentiment (positive, negative, neutral) of the news headlines.

3. **DecisionMakerAgent**  
   Makes a decision based on sentiment analysis — whether to BUY, SELL, or HOLD.

---
## 🛠️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/AmeyDikshit23/stock-multi-agent-system.git
cd stock-multi-agent-system

📦 Dependencies
requests

beautifulsoup4

textblob or vaderSentiment

nltk (if using certain sentiment tools)

pip install -r requirements.txt

🧪 Sample Query

Enter stock ticker: TSLA
Example Output:
Fetching news for TSLA...
Top headline: Tesla stock soars after strong delivery numbers
Sentiment: Positive
Decision: BUY
