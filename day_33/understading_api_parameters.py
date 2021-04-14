import requests
from datetime import datetime

# Constant Variables
# London
MY_LAT = 51.507351
MY_LONG = -0.127758

# APIs have endpoints, which is the equivalent of the address of the place we
# want to get data from or communicate with.

# APIs also have parameters. This is a way to give inputs when we are making
# API requests so that we can receive different kinds of data depending on
# the inputs (the same way we give inputs/parameters to functions to get
# different outputs).

# Not all APIs have parameters. Some are really simple, like the ISS API.
# Others do allow to provide parameters, like the Sunset-Sunrise API
# (https://sunrise-sunset.org/api) which gives us the times for the sunset
# and sunrise at specified locations.

# Using the Sunset-Sunrise API (we must provide longitude and latitude
# coordinates as parameters)
parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0
}

response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
print(data)

# With these .split() methods, we will just get the hour of sunrise and sunset
sunrise = data["results"]["sunrise"].split('T')[1].split(':')[0]
sunset = data["results"]["sunset"].split('T')[1].split(':')[0]
print(f"Sunrise hour: {sunrise}\nSunset hour: {sunset}")

time_now = datetime.now()
print(f"Current hour from the datetime module: {time_now.hour}")
