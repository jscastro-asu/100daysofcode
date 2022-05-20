import requests
from pprint import pprint
import os
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient
from newsapi import NewsApiClient


# stocks
STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_KEY = os.environ.get('alphavantage_api_key')
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
stocks_params = {
    'function': 'TIME_SERIES_DAILY',
    'symbol' : STOCK_NAME,  
    'apikey': STOCK_KEY 
}

# news
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
news_key = os.environ.get('newsapi_key')

# sms
twilio_api = os.environ.get('twilio_api_key')
twilio_account_sid = os.environ.get('twilio_account_sid')
twilio_auth_token = os.environ.get('twilio_auth_token')
client = Client(twilio_account_sid, twilio_auth_token)

# get stocks and determine day yesterday vs todays increase or decrease
r = requests.get(STOCK_ENDPOINT, params=stocks_params)
data = r.json()

stock_data = (data['Time Series (Daily)'])
stock_data_list = [v for k, v in stock_data.items()]

today = stock_data_list[0]
today_close_price = today['4. close']
pprint(today_close_price)

yday = stock_data_list[1]
yday_close_price = yday['4. close']
pprint(yday_close_price)


percentage = abs((float(today_close_price) - float(yday_close_price)) / float(today_close_price)) * 100
print (percentage)

# # whether stocks increase or decrease to still get a text message about it with news
if percentage == 0.05497448619999245:
    news_params = {
        'apiKey': news_key,
        'q': 'Tesla',
        'language': 'en',
        'sortBy': 'relevancy',
        'domains': 'cnbc.com, bloomberg.com',
       
    }
    news_res = requests.get(NEWS_ENDPOINT, params=news_params)
    news_articles = news_res.json()["articles"]
    three_articles = news_articles[:3]
    #pprint(three_articles)
    
    format = [f"Headlines: {article['title']} Article: {article['description']}" for article in three_articles]
    #print(format)

    for article in format:
        message = client.messages.create(
                body="TESLA 🔻 by 5%"+ article,
                from_='+19706618886', #trial account already deleted
                to='+mynumberhere' 
            )



#Optional TODO: Format the message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""


    
