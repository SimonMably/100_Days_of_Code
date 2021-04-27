import requests
import datetime as dt
import os
from dotenv import load_dotenv

load_dotenv()
APP_ID = os.getenv("APP_ID")
API_KEY = os.getenv("API_KEY")
SHEET_ENDPOINT = os.getenv("SHEET_ENDPOINT")
TOKEN = os.getenv("TOKEN")

nutritionix_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

nutrition_parameters = {
    "query": input("What exercise have you done? ").title(),
}

# "gender": "",  # optional
# "weight_kg": 0,  # optional
# "height_cm": 0,  # optional
# "age": 0  # optional

nutrition_headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "x-remote-user-id": "0",
    "content-type": "application/json",
}

response = requests.post(url=nutritionix_endpoint, json=nutrition_parameters,
                         headers=nutrition_headers)
print(response.status_code)

print(response.json())


sheet_endpoint = SHEET_ENDPOINT

sheet_auth = {
    "Authorization": TOKEN
}

date_time = dt.datetime.now()
date = date_time.strftime("%d/%m/%Y")
time = date_time.strftime("%X")

sheet_parameters = {
    "workout": {
        "date": date,
        "time": time,
        "exercise": response.json()["exercises"][0]["user_input"].title(),
        "duration": response.json()["exercises"][0]["duration_min"],
        "calories": response.json()["exercises"][0]["nf_calories"],
    }
}

add_data = requests.post(url=sheet_endpoint, json=sheet_parameters,
                         headers=sheet_auth)

