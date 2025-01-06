from twilio.rest import Client
import requests
from datetime import datetime

class StockAnalyzer:
    def __init__(self, stock_symbol, alpha_vantage_key):
        self.stock = stock_symbol
        self.api_key = alpha_vantage_key
        
    def get_price_change(self):
        url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={self.stock}&apikey={self.api_key}"
        response = requests.get(url).json()
        data = response["Time Series (Daily)"]
        dates = list(data.keys())[:2]
        
        price_change = (float(data[dates[0]]["1. open"]) - float(data[dates[1]]["2. high"])) / float(data[dates[0]]["1. open"]) * 100
        return price_change

class NewsCollector:
    def __init__(self, company_name, news_api_key):
        self.company = company_name
        self.api_key = news_api_key
        
    def get_news(self):
        url = f"https://newsapi.org/v2/everything?q={self.company}&language=en&sortBy=publishedAt&apiKey={self.api_key}"
        response = requests.get(url).json()
        
        news = []
        for article in response["articles"][:3]:
            news.append({
                "title": article["title"],
                "description": article["description"]
            })
        return news

class NotificationManager:
    def __init__(self, account_sid, auth_token, from_number, stock=None):  # Add stock parameter
        self.client = Client(account_sid, auth_token)
        self.from_number = from_number
        self.stock = stock  # Store stock symbol
        
    def send_notification(self, to_number, price_change, news):
        arrow = "🔺" if price_change > 0 else "🔻"
        message = f"{self.stock}: {arrow}{abs(price_change):.2f}%\n\n"
        
        for article in news:
            message += f"Headline: {article['title']}\nBrief: {article['description']}\n\n"
            
        self.client.messages.create(
            body=message,
            from_=self.from_number,
            to=to_number
        )

def main():
    # Configuration
    STOCK = "Stock name" #example "AAPL"
    COMPANY_NAME = "Company name" #example "apple"
    ALPHA_VANTAGE_KEY = "api from this website" # get api from  https://www.alphavantage.co/
    NEWS_API_KEY = "api for this website " # u can get api from https://newsapi.org/
    TWILIO_SID = "twilio account sid" #i used twilio to create number and send smss i advise to check this website
    # u can find bunch cool stuff u can do like sending automatic sms like i did https://www.twilio.com/en-us
    TWILIO_TOKEN = "twilio account token"
    FROM_NUMBER = "twilio account number "
    TO_NUMBER = "to the number u want to send"
    PRICE_THRESHOLD = 5.0  # 5% change threshold

    # Initialize components
    stock_analyzer = StockAnalyzer(STOCK, ALPHA_VANTAGE_KEY)
    news_collector = NewsCollector(COMPANY_NAME, NEWS_API_KEY)
    notifier = NotificationManager(TWILIO_SID, TWILIO_TOKEN, FROM_NUMBER, STOCK)
    # Check stock price change
    price_change = stock_analyzer.get_price_change()
    
    # If price change exceeds threshold, get news and send notification
    if abs(price_change) >= PRICE_THRESHOLD:
        news = news_collector.get_news()
        notifier.send_notification(TO_NUMBER, price_change, news)

if __name__ == "__main__":
    main()