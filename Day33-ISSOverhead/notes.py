# Notes on APIs

# Your Program |API| External System (works via requests)
# Request ---> <--- Response

# An API Endpoint: the location where the data is literally, electronically stored. ex. API.coinbase.com
# Some APIs need express permission to use, guides,
# or outright don't allow you to access ever, or sometimes. (just look)

import requests  # https://docs.python-requests.org/en/latest/

response = requests.get(url="http://api.open-notify.org/iss-now.json")
print(response.status_code)
# if your response code is 1**: hold on, 2**: good, 3**: blocked, 4**: your error, 5**: their error

response.raise_for_status()  # https://www.webfx.com/web-development/glossary/http-status-codes/

data = response.json()  # actual data given by API
print(data)

longitude = response.json()["iss_position"]["longitude"]
latitude = response.json()["iss_position"]["latitude"]
iss_position = (longitude, latitude)  # https://www.latlong.net/Show-Latitude-Longitude.html
print(iss_position)

# Kanye Quotes App using Kanye Rest API https://kanye.rest on kanye.py
print("\n")

# Sunrise and Sunset Times  https://sunrise-sunset.org/api
from datetime import datetime

MY_LAT = 51.507351
MY_LONG = -0.127758

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]  # https://www.w3schools.com/python/ref_string_split.asp
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]

print(sunrise)
print(sunset)

time_now = datetime.now()

print(time_now.hour)

# continues in actual ISS project, main.py
