import requests
from time import gmtime, strftime

# DATE 05/21/22,TIME 03:55:12 AM
d = strftime("%d/%m/%Y")
t = strftime("%r ", gmtime())

GENDER = "Female"
WEIGHT = 68
HEIGHT = 160
AGE = 33

ID = 'cd024214'
KEY = 'f5f1a3093b0be9d2ee78a16fffe562d9'

headers = {
    'x-app-id': ID,
    'x-app-key': KEY
}

endpoint = 'https://trackapi.nutritionix.com/v2/natural/exercise'
sheety_endpoint = 'https://api.sheety.co/2b7fcdd23efec81c0733a53af4d2582e/myWorkouts/workouts'
text = input("Enter today's workout: ")

entry = {
    "query": text,
    "gender": GENDER,
    "weight_kg": WEIGHT,
    "height_cm": HEIGHT,
    "age": AGE
}

resp = requests.post(url=endpoint, json=entry, headers=headers)
resp.raise_for_status()
result = resp.json()

# -----

for exercise in result["exercises"]:
    my_log = {
        "workout":
            {
                "date": d,
                "time": t,
                "exercise": exercise['name'].title(),
                "duration": exercise['duration_min'],
                "calories": exercise['nf_calories']
            }
    }

    log_resp = requests.post(url=sheety_endpoint, json=my_log)
    log_result = log_resp.text
    print(log_result)

