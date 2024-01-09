# Rain Alert App using https://openweathermap.org/current
# 'etc' used to notate where you must use your own information, and obviously not mine!

import os
import requests
from twilio.rest import Client

api_key = "80644bdb613aa9etc"  # make your own account and use your own key, else it won't work!
OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
account_sid = os.environ['ACc51513aad77505etc']
auth_token = os.environ['0d511fd4909adetc']

weather_params = {
    "lat": 51.507351,
    "lon": -0.127758,
    "appid": api_key,
    "cnt": 4
}

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()

# print(weather_data["list"])  View these via https://jsonviewer.stack.hu/
# print(weather_data["list"][0]["weather"][0]["id"]) shows '804'

will_rain = False
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(body="It's going to rain today. Remember to bring an umbrella!",
                from_='+1833etc', to='+1248etc')  # use your verified personal number
    print(message.status)

