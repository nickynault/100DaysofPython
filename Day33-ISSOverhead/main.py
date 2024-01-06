# ISS Overhead

import requests
from datetime import datetime
import smtplib
import time

MY_LAT = 51.507351
MY_LONG = -0.127758
EMAIL = "appbrewery@gmail.com"
PASSWORD = "abcd123()"


def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    if MY_LAT-5 <= iss_latitude <= MY_LAT+5 and MY_LONG-5 <= iss_longitude <= MY_LONG+5:  # compare our coords to iss
        return True


def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0
    }

    response1 = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response1.raise_for_status()
    data1 = response1.json()
    sunrise = int(data1["results"]["sunrise"].split("T")[1].split(":")[0])  # https://www.w3schools.com/python/ref_string_split.asp
    sunset = int(data1["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour

    if time_now >= sunset or time_now <= sunrise:  # check current time vs sunrise/sunset times
        return True
    
    
while True:
    time.sleep(60)  # only runs every 60 seconds
    
    if is_iss_overhead() and is_night():  # check for both
        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(EMAIL, PASSWORD)
        connection.sendmail(
            from_addr=EMAIL,
            to_addrs=EMAIL,
            msg="Subject:Look Up!\n\nThe ISS is above you in the sky."  # when they line up, you get an email
        )
    
