import requests

# API Endpoint:
# We an imagine API Endpoints as locations.

# If we want data from a particular external service, then we need to know at
# what location the data is stored. For example, if we wanted to get money
# out of a bank, we need to know where the bank is first before we go there.
# In terms of API lingo, this known as a API Endpoint. Usually, these API
# Endpoints are URLS (eg, 'api.coinbase.com' for crypto data - this is the
# location where the Coinbase data can be found)


# API Request:
# Requesting data from the API Endpoint.

# Analogy:
# API Requests are similar to going to the bank and trying to withdraw some
# money from their vaults (or getting data from an API Endpoint). Banks also
# employ bank tellers to ask questions and make some checks (to make sure
# that people have a right to withdraw the money).
# In this analogy, the bank teller is like an API. It's the interface between
# us and the bank vault. We can ask a bank teller to withdraw some money,
# but that would involve checking for an id, an account number and some other
# checks. We could also ask the bank teller questions that doesn't require
# any authentication, such as asking about opening hours. This is the
# equivalent of a ver simple 'get' request, where we just get a piece of data
# from a website/app using an API.


# Working with APIs (eg. International Space Agency Current Location API):
# Retrieving the current location of the ISS (International Space Station)

# API Endpoint for this particular API:
# http://api.open-notify.org/iss-now.json

# The API Endpoint returns the output data in the form of JSON format. This is
# quite common when dealing with APIs.

# If we want to make a request to an API, we have the option of using a web
# browser to do it. We simply copy the API Endpoint and paste it into the web
# browsers search bar and the browser will return the data in the JSON
# format. At every refresh of the page will mean a new API request.

# The reason APIs use JSON is because it is quick and easy transfer over the
# internet.

# Making and API request (using the requests library):

# API Endpoint (as a string) is used as 'url' keyword argument:
response = requests.get(url="http://api.open-notify.org/iss-now.json")
# Prints a response code, not JSON data
print(response)
# For responses, see 'working_with_responses.py'
