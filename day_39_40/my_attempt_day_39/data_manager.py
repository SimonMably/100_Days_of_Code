from dotenv import load_dotenv
import os
import requests


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        load_dotenv()
        self.TOKEN = os.getenv("SHEET_TOKEN")
        self.SHEET_ENDPOINT = os.getenv("SHEET_ENDPOINT")
        self.header = {"Authorization": self.TOKEN}
        self.destination_data = {}

    def get_response(self):
        """Get request for Google Sheet data. Returns response."""
        response = requests.get(url=self.SHEET_ENDPOINT, headers=self.header)
        return response.json()["prices"]

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }

            header = {
                "Authorization": self.TOKEN
            }

            response = requests.put(
                url=f"{self.SHEET_ENDPOINT}/{city['id']}",
                json=new_data, headers=header

            )
            print(response.text)
