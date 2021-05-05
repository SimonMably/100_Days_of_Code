# from pprint import pprint
import requests
from dotenv import load_dotenv
import os

load_dotenv()
SHEETY_PRICES_ENDPOINT = os.getenv("SHEETY_PRICES_ENDPOINT")
SHEETY_USERS_ENDPOINT = os.getenv("SHEETY_USERS_ENDPOINT")
SHEETY_TOKEN = os.getenv("SHEET_TOKEN")


class DataManager:

    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        """Sends get request via Sheety. Retrieves relevant destination data."""
        header = {
            "Authorization": SHEETY_TOKEN,
        }

        response = requests.get(url=SHEETY_PRICES_ENDPOINT, headers=header)
        data = response.json()
        self.destination_data = data["price"]
        return self.destination_data

    def update_destination_codes(self):
        """Sends get request via Sheety. Updates relevant fields with AITA
        codes."""
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }

            header = {
                "Authorization": SHEETY_TOKEN,
            }

            response = requests.put(
                url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",
                json=new_data, headers=header
            )
            print(response.text)

    def get_customer_emails(self):
        customers_endpoint = SHEETY_USERS_ENDPOINT
        response = requests.get(url=customers_endpoint)
        data = response.json()
        self.customer_data = data["users"]
        return self.customer_data
