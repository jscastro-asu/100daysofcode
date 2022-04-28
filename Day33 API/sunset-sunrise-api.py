import requests
from datetime import datetime
now = datetime.now()

res = requests.get(url='https://api.sunrise-sunset.org/json?lat=10.6840&lng=122.9563&date=2022-04-16')
res.raise_for_status()

data = res.json()
sunrise = data["results"]["sunrise"]
sunset = data["results"]["sunset"]
timenow = now.strftime("%m/%d/%Y, %I:%M:%S %p")
print(f"BACOLOD CITY, PHIL TODAY {timenow} \nSunrise: {sunrise} Sunset: {sunset}")
