import requests
from datetime import datetime
import smtplib as smtp
import os
from dotenv import load_dotenv
import time

# Latitude and longitude for London
MY_LAT = 51.507351
MY_LONG = -0.127758


def iss_is_above():
    """Requests position of ISS via ISS position API. Checks ISS position is
    within 5 degrees (latitude and longitude) of specified position."""
    iss_response = requests.get(url="http://api.open-notify.org/iss-now.json")
    iss_response.raise_for_status()
    iss_data = iss_response.json()

    iss_latitude = float(iss_data["iss_position"]["latitude"])
    iss_longitude = float(iss_data["iss_position"]["longitude"])

    if MY_LAT-5 <= iss_latitude <= MY_LAT+5 and MY_LONG-5 <= iss_longitude <= MY_LONG+5:
        return True
    else:
        return False


def is_night():
    """"""
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    sun_response = requests.get("https://api.sunrise-sunset.org/json",
                                params=parameters)
    sun_response.raise_for_status()
    sun_data = sun_response.json()
    sunrise = int(sun_data["results"]["sunrise"].split("T")[1].split(":")[0])+1
    sunset = int(sun_data["results"]["sunset"].split("T")[1].split(":")[0])+1

    time_now = datetime.now()

    if time_now.hour >= sunset or time_now.hour >= sunrise:
        return True


while True:
    time.sleep(60)
    if iss_is_above() and is_night():
        load_dotenv()
        email = os.getenv("EMAIL")
        password = os.getenv("PASSWORD")

        connection = smtp.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(user=email, password=password)
        connection.sendmail(from_addr=email, to_addrs=email,
                            msg="Subject:ISS Position\n\nThe ISS is above "
                                "in the sky.")

        print("Email sent!")
