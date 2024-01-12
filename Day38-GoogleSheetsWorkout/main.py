# Google Sheets Workout main.py - https://www.nutritionix.com/business/api
# https://docs.google.com/document/d/1_q-K-ObMTZvO0qUEAxROrN3bwMujwAN25sLHwJzliK0/preview
# https://sheety.co/docs/requests

import requests
import os
from datetime import datetime

EXERCISE_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
NUTRITION_API_KEY = "ea556f47276etc"  # create your own on nutritionix
NUTRITION_APP_ID = "1b8etc"  # same as above, get your own
SHEETY_ENDPOINT = "https://api.sheety.co/your_username/Copy of My Workouts/Copy of My Workouts"  # create your own on sheety
GOOGLE_SHEET_NAME = "workout"
sheety_inputs = {}

nutrition_headers = {
    "x-app-id": NUTRITION_APP_ID,
    "x-app-key": NUTRITION_API_KEY,
}

nutrition_params = {
    "query": input("Tell me which exercise you did: "),
    "weight_kg": input("What is your weight? (kg) "),
    "height_cm": input("What is your height? (cm) "),
    "age": input("How old are you? "),
}

nutrition_response = requests.post(EXERCISE_ENDPOINT, json=nutrition_params, headers=nutrition_headers)
result = nutrition_response.json()
print(result)

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheety_inputs = {
        "date": today_date,
        "time": now_time,
        "exercise": exercise["name"].title(),
        "duration": exercise["duration_min"],
        "calories": exercise["nf_calories"]
    }

sheety_response = requests.post(SHEETY_ENDPOINT, json=sheety_inputs)
print(sheety_response.text)
