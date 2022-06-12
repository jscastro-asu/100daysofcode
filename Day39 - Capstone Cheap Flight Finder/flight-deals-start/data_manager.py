import requests

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    sheety_endpoint = "https://api.sheety.co/2b7fcdd23efec81c0733a53af4d2582e/flightDeals/prices"
    sheety_param = {
        "price": {
            "city": "city",
            "iata code": "",
            "lowest_price": ""
        }
    }
    sheety = requests.get(url=sheety_endpoint, json=sheety_param)
    print(sheety)
