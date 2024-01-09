# Stock Trading Alert Project, main.py
# active Tesla stock - https://www.tradingview.com/symbols/NASDAQ-TSLA/
# 'etc.' used to notate where you must use your own information, and obviously not mine!

import requests
from twilio.rest import Client

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_API_KEY = "1NCBI8etc"  # use your own via https://www.alphavantage.co/support/#api-key
NEWS_API_KEY = "c3d807beetc"  # use your own via https://newsapi.org/account
TWILIO_SID = "ACc51513aadetc"  # use your own via https://console.twilio.com
TWILIO_AUTH = "5e0b8d757etc"  # use your own via https://console.twilio.com

stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY
}

# grab all the data from the API
response = requests.get(STOCK_ENDPOINT, params=stock_params)
response.raise_for_status()
data = response.json()["Time Series (Daily)"]
data_list = [value for (key, value) in data.items()]

# yesterday's closing stock price
yesterday_data = data_list[0]
yesterdays_closing_price = yesterday_data['4. close']
print(f"\nYesterday's closing stock price was ${yesterdays_closing_price}.")

# day before yesterday's closing stock price
day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = day_before_yesterday_data['4. close']
print(f"The day before yesterday's closing stock price was ${day_before_yesterday_closing_price}.")

# find difference and force it to be positive
difference = abs(float(yesterdays_closing_price) - float(day_before_yesterday_closing_price))
print(f"The difference between the days is ${difference}.")

# find the percentage difference between the days
diff_percent = (difference / float(yesterdays_closing_price))
print(f"The percentage difference is {diff_percent}%.")

# if percent is over some number, grab news about the stock
if diff_percent > 0:
    news_params = {
        "apiKey": NEWS_API_KEY,
        "qInTitle": COMPANY_NAME,
    }

    response1 = requests.get(NEWS_ENDPOINT, params=news_params)
    response1.raise_for_status()
    articles = response1.json()["articles"]

    # slice and create a list with first 3 articles and grab headlines
    three_articles = articles[:3]
    formatted_articles = [f"Headline: {article['title']}. \nBrief: {article['description']}" for article in three_articles]

    # setup twilio stuff
    client = Client(TWILIO_SID, TWILIO_AUTH)

    # send each article as separate messages via SMS
    for article in formatted_articles:
        message = client.messages.create(
            body=article,
            from_="+1833etc",
            to="+1248etc"  # use your own numbers
        )
