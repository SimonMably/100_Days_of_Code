from dotenv import load_dotenv
import os
import requests
import datetime as dt
from flight_data import FlightData


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    def __init__(self):
        load_dotenv()
        self.FLIGHT_SEARCH_API = os.getenv("FLIGHT_SEARCH_APIKEY")
        self.tequila_endpoint = "https://tequila-api.kiwi.com"
        self.departure_city = "DEN"

    def retrieve_iata_code(self, city_name):
        """Makes get request from Kiwi Partners Tequila API, retrieves
        International Air Transport Association (IATA) code for cities in
        Google Sheet."""
        location_endpoint = f"{self.tequila_endpoint}/locations/query"

        params = {
            "term": city_name,
            "location_types": "city"
        }

        header = {
            "apikey": self.FLIGHT_SEARCH_API
        }

        response = requests.get(url=location_endpoint, headers=header,
                                params=params)
        results = response.json()["locations"]
        code = results[0]["code"]
        return code

    def search_flights(self, destination_code):
        """Interacts with the Tequila Flight Search API to search for flights
        between London and destinations defined in Google Sheets for a 6
        month period. Returns cost for each flight if direct flights
        available. Cost of flights represented in GBP."""
        now = dt.datetime.now()
        tomorrow = now + dt.timedelta(days=1)
        in_six_months = tomorrow + dt.timedelta(weeks=26)

        location_endpoint = f"{self.tequila_endpoint}/v2/search"

        params = {
            "fly_from": self.departure_city,
            "fly_to": destination_code,
            "dateFrom": tomorrow.strftime("%d/%m/%Y"),
            "dateTo": in_six_months.strftime("%d/%m/%Y"),
            "return_in_dst_from": 7,
            "return_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "USD",
        }

        header = {
            "apikey": self.FLIGHT_SEARCH_API
        }

        response = requests.get(url=location_endpoint, params=params,
                                headers=header)
        try:
            data = response.json()["data"][0]
        except IndexError:
            print(f"No flights to {destination_code}")
            return None

        flight_data = FlightData(
            price=data["price"],
            departure_city=data["route"][0]["cityFrom"],
            departure_airport_code=data["route"][0]["flyFrom"],
            departure_date=data["route"][0]["local_departure"].split("T")[0],
            arrival_city=data["route"][0]["cityTo"],
            arrival_city_code=data["route"][0]["flyTo"],
            return_date=data["route"][1]["local_departure"].split("T")[0],
        )

        print(f"{flight_data.departure_city}: ${flight_data.price} USD")

        return flight_data













