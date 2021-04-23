import requests
from twilio.rest import Client
import os
from dotenv import load_dotenv

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

load_dotenv()
AV_API_KEY = os.getenv("ALPHA_VANTAGE_API_KEY")
NEWS_API = os.getenv("NEWS_API")
SMS_API_KEY = os.getenv("TWILIO_API_KEY")
ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
SENDER = os.getenv("SENDER")
RECIPIENT = os.getenv("RECIPIENT")

# Alpha Advantage API request example:
# https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=TSLA&apikey=R4QKC71GFAS4VVGV

# STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day
# before yesterday then print("Get News").

stock_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": AV_API_KEY,
}

stock_response = requests.get(STOCK_ENDPOINT, params=stock_parameters)
stock_response.raise_for_status()
data = stock_response.json()["Time Series (Daily)"]

# TODO 1. - Get yesterday's closing stock price. Hint: You can perform list
#           comprehensions on Python dictionaries. e.g. [new_value for (key,
#           value) in  dictionary.items()]
data_list = [value for (key, value) in data.items()]

yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data["4. close"]

day_before_data = data_list[1]
day_before_closing_price = day_before_data["4. close"]

difference = float(yesterday_closing_price) - float(day_before_closing_price)
up_down = None
if difference > 0:
    up_down = "⬆️"
else:
    up_down = "⬇️"


perc_increase = round(float(difference) / float(yesterday_closing_price) * 100)

if abs(perc_increase) > 1:
    news_parameters = {
        "qInTitle": COMPANY_NAME,
        "apiKey": NEWS_API,
    }
    news_response = requests.get(NEWS_ENDPOINT, params=news_parameters)

    latest_news = news_response.json()["articles"][:3]

    headlines = [f"{STOCK_NAME}: {up_down}{perc_increase}%\n"
                 f"Headline: {article['title']}. \n"
                 f"Brief: {article['description']}" for article in latest_news]

    client = Client(ACCOUNT_SID, AUTH_TOKEN)

    for article in headlines:
        message = client.messages.create(
            body=article,
            from_=SENDER,
            to=RECIPIENT
        )


# Optional TODO: Format the message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?.
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?.
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""
