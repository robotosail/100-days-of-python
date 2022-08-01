# getting stock prices
import requests
import os

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
STOCK_APIKEY = "7LXT0NC8QWMRJL9F"
stock_url = 'https://www.alphavantage.co/query'
NEWS_APIKEY = "8cf9105cbea24efcb54e5ef6a62cb3fd"
news_url = "https://newsapi.org/v2/everything?"


STOCK_Params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    # "apikey": "demo"
    "apikey": STOCK_APIKEY
}

news_params = {
    "apiKey": NEWS_APIKEY,
    "qInTitle": COMPANY_NAME,

}

# getting the data
response = requests.get(url=stock_url, params=STOCK_Params)
response.raise_for_status()

# Get yesterday's closing stock price.
data = response.json()["Time Series (Daily)"]
data_list = [value for (key, value) in data.items()]
yesterday = data_list[0]
yestrdy_closing = data_list[0]["4. close"]
# print(yestrdy_closing)
# Get the day before yesterday's closing stock price
day_bf_yestr = data_list[1]
day_bf_yestr_price = day_bf_yestr["4. close"]
# print(day_bf_yestr_price)

# Find the positive difference between 1 and 2. e.g. 40 - 20 = -20,
difference = float(yestrdy_closing) - float(day_bf_yestr_price)

up_down = None
if difference > 0:
    up_down = "⬆️"
else:
    up_down = "🔻"

# Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.
percent = round(difference / float(yestrdy_closing) * 100)
print(abs(percent))

# - If TODO4 percentage is greater than 5 then print("Get News").
if abs(percent) > -1:
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
    news_response = requests.get(news_url, params=news_params)
    news_response.raise_for_status()
    articles = news_response.json()["articles"]
    # slising to create a list of the first 3 articles
# Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation
    three_articles = articles[:3]

# to send a separate message with each article's title and description to your phone number.
# - Create a new list of the first 3 article's headline and description using list comprehension.
    formated_articles = [
        f"{STOCK_NAME}: {up_down} {percent}% \n Headline: {article['title']}. \nBrief: {article['description']}" for article in three_articles]

    print(formated_articles)

# TODO 9. - Send each article as a separate message via Twilio.
