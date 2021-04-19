import requests
from twilio.rest import Client


owm_endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = "1aded3bf923268f713cfc066ea331251"
account_sid = "ACbddc3b6cad8cb62f86b6e048f9256940"
auth_token = "e9e00595ba6ec9857653dcac8882057a"

parameters = {
    "lat": 50.828423,
    "lon": -0.152584,
    "appid": api_key,
    "exclude": "current,minutely,daily"
}

response = requests.get(url=owm_endpoint, params=parameters)
response.raise_for_status()

weather_data = response.json()

will_rain = False

for hour in weather_data["hourly"][:12]:
    weather_condition = hour["weather"][0]["id"]
    if weather_condition <= 900:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body="It's raining today. Remember to bring an umbrella.",
        from_="+15053862916",
        to="+447413438802"
    )
    print(message.status)










