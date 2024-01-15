# This class is responsible for talking to the Google Sheet.

import requests
from pprint import pprint

SHEETY_API = "https://api.sheety.co/686d9c760634acdc6102b3a36a6d462d/flightDeals/prices"
SHEETY_NAME = "FlightDeals"


class DataManager:
    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(url=SHEETY_API)
        data = response.json()
        self.destination_data = data["prices"]

        pprint(self.destination_data)

        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_API}/{city['id']}",
                json=new_data
            )
            print(response.text)
