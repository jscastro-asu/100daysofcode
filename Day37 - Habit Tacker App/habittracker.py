import requests
import time
from datetime import datetime, timedelta

TOKEN = 'Learningpython101'
DATE = time.strftime('%Y%m%d') # today - use to add pixels
yesterday = datetime.now() - timedelta(1) # yesterday - use to add pixels
YDAY = datetime.strftime(yesterday, '%Y%m%d')



# authentication
headers = {
    'X-USER-TOKEN': TOKEN
}

pixela_endpoint = 'https://pixe.la/v1/users'
user_params = {
    'token': TOKEN,
    'username': 'jennielyn',
    'agreeTermsOfService':'yes',
    'notMinor':'yes'
}

# response1 = requests.post(url=pixela_endpoint, json=user_params)
# print(response1.text)
graph_endpoint = 'https://pixe.la/v1/users/jennielyn/graphs'
graph_params = {
    'id': 'habittracker',
    'name': 'Exercise Tracker Graph',
    'unit': 'commit',
    'type': 'int',
    'color':'shibafu'
}

# response2 = requests.post(url=graph_endpoint, json=graph_params, headers=headers)
# print(response2.text)
post_pix = 'https://pixe.la/v1/users/jennielyn/graphs/habittracker'
pixel_params = {
    'date': DATE,
    'quantity': input("Minutes you exercise today? ")
}

response3 = requests.post(url=post_pix, json=pixel_params, headers=headers)
print(response3.text)
