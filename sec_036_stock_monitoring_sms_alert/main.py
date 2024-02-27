import requests
import datetime as dt
from twilio.rest import Client
import os

# stocks api
STOCK = "TSLA"
AV_API_KEY = os.environ.get("ALPHA_VAN_API_KEY")

# news api
NEWS_API_KEY = os.environ.get("NEWS_API_KEY")
COMPANY_NAME = "Tesla Inc"

# twillio api
AUTH_TOKEN = os.environ.get("TWILLIO_AUTH_TOKEN") 
ACCOUNT_SID = os.environ.get("TWILLIO_ACCOUNT_SID")


#---------------------------------------------------------------------------------#
day_of_week = dt.datetime.now().weekday()

if day_of_week != 0 or day_of_week != 6:
    stock_requests_parameters = {
        "function":"TIME_SERIES_DAILY",
        "symbol": STOCK,
        "apikey": AV_API_KEY,
        "datatype": "json",
    }

    stock_response = requests.get("https://www.alphavantage.co/query", params=stock_requests_parameters)
    stock_response.raise_for_status()
    stock_data = stock_response.json()["Time Series (Daily)"]
    days = list(stock_data.keys())
    yesterday_close_value = float(stock_data[days[0]]["4. close"])
    the_day_before_close_value  = float(stock_data[days[1]]["4. close"])

    increase = (the_day_before_close_value/yesterday_close_value)*100
    rounded_increase_value = round(increase-100, 2)

    if not (-7.5 <= increase <= 7.5):
        news_parameters = {
            "apiKey": NEWS_API_KEY,
            "q": COMPANY_NAME,
            "from": dt.datetime.now().date() - dt.timedelta(days=3),
            "to": dt.datetime.now().date(),
            "sortBy": "popularity"
        }

        news_response = requests.get("https://newsapi.org/v2/everything", params=news_parameters)
        news_response.raise_for_status()
        news = news_response.json()
        three_popular_articles = news["articles"][:3]
        for article in three_popular_articles:
            headline = article["title"].strip()
            brief = article["description"].strip()

            # send messages via Twillio    
            client = Client(ACCOUNT_SID, AUTH_TOKEN)
            message = client.messages \
                .create(
                    body = f"{COMPANY_NAME}: {rounded_increase_value}%\nHeadline: {headline}\nBrief: {brief}",
                    from_ = "+13253134794",
                    to = os.environ.get("MY_NUMBER")
                )





