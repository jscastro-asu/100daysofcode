# use of weather API
# parsing 
# send me a text message
# this is in pythonanywhere to set up a cron job and schedule to send message every 7am for ex

import requests
import json
from pprint import pprint  # to print in a readable json

import os
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient


api_key = 'eb07149c32dbbd6e36a656dcd475' #fake api key
url = 'https://api.openweathermap.org/data/2.5/onecall'

# twilio
account_sid = os.environ['AC2c3e572c97581c41e7f02463474a68f5']
auth_token = os.environ['4aa8dfa0d7e5aa929cadc1839b35ed38']
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="Join Earth's mightiest heroes. Like Kevin Bacon.",
                     from_='+19706618886',
                     to='+12069004567'
                 )

print(message.sid)


weather_params = {
'lat': 47.191952,
'lon': -122.180687,
'appid': api_key,
'exclude': 'current,minutely,daily',
'units': 'imperial',
'timezone': 'America/Los Angeles'
}

response = requests.get(url, params=weather_params)
response.raise_for_status()
weather_data = response.json()

# accessing hourly's and slicing to get the id value e.g: 500 light rain
# weather_id = (weather_data['hourly'][0]['weather'][0]['id'])


# slicing hourly to first 12 hours
weather_slice = weather_data['hourly'][:12]
for hour in weather_slice:
    # picking just the id from the dict
    cond_code = hour["weather"][0]['id']
    # picking rain type
    desc = hour["weather"][0]['description']
    
    if int(cond_code) < 700:
        proxy_client = TwilioHttpClient()
        proxy_client.session.proxies = {'https': os.environ['https_proxy']}
        client = Client(account_sid, auth_token, http_client=proxy_client)

        message = client.messages.create(
            body="⚠️ Reminder ⚠️ : It's going to rain bring umbrella 🌧️ ☔ 🌧️ !",
            from_='+ you twilio generated num', # trial num
            to='+ your verified num' # trial num
        )

    print(message.sid)
    
