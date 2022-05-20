# use of weather API
# parsing jsons


import requests
import json
from pprint import pprint  # to print in a readable json



api_key = 'eb07149c32dbbd6e36a656dcd475' # fake api key
url = 'https://api.openweathermap.org/data/2.5/onecall'


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

# I only need it to print once
to_rain = False
# slicing hourly to first 12 hours
weather_slice = weather_data['hourly'][:12]
for hour in weather_slice:
    # picking just the id from the dict
    cond_code = hour["weather"][0]['id']
    # picking rain type
    desc = hour["weather"][0]['description']
    
    if int(cond_code) < 700:
        to_rain = True
print(f"Bring umbrella. It is a {desc}.")
 



    