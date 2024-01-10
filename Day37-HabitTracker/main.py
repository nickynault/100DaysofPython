# Habit Tracker main.py
# we'll use Pixela  https://requests.readthedocs.io/en/latest/api/  https://docs.pixe.la/

import requests
from datetime import datetime

today = datetime.now()
PIXELA_ENDPOINT = "https://pixe.la/v1/users"
USERNAME = "nicketc"
TOKEN = "jkdawdfwlakf213etc"
GRAPH_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"
PIXELA_CREATION_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/graph1"
UPDATE_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/graph1/{today.strftime('%Y%m%d')}"
DELETE_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/graph1/{today.strftime('%Y%m%d')}"

user_params = {
    "token": TOKEN,  # literally make this up, between 8-120 chars
    "username": USERNAME,  # make up your own that no one else has taken
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# Create your account
# response = requests.post(url=PIXELA_ENDPOINT, json=user_params)         do this once and then not again
# print(response.text)

# Create a graph definition
graph_config = {
    "id": "graph1",  # must start with letter. then 1-16 chars
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai"  # pixela is in japanese (this is purple)
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=GRAPH_ENDPOINT, json=graph_config, headers=headers)
# print(response.text)

# Create a plot on the graph
pixel_data = {
    "date": today.strftime("%Y%m%d"),  # https://www.w3schools.com/python/python_datetime.asp
    "quantity": input("How many kilometers did you cycle today?"),
}

# response = requests.post(url=PIXELA_CREATION_ENDPOINT, json=pixel_data, headers=headers)
# print(response.text)

# Update a pixel
new_pixel_data = {
    "quantity": input("How many kilometers did you actually cycle today?"),
}

# response = requests.put(url=UPDATE_ENDPOINT, json=new_pixel_data, headers=headers)
# print(response.text)

# Delete a pixel
# response = requests.delete(url=DELETE_ENDPOINT, headers=headers)
# print(response.text)

# REMEMBER: THESE NEED TO BE DONE ONE AT A TIME. IT WON'T WORK IF YOU JUST TRY TO DELETE BEFORE HAVING AN ACCOUNT!

