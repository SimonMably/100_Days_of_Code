import requests

# Response Code 404 means that whatever we are looking for doesn't exist.

# API Endpoint (as a string) is used as 'url' keyword argument:
response = requests.get(url="http://api.open-notify.org/iss-now.json")
# Prints '<Response [200]'
print(response)

# Response code meanings:
# 100 - 199: Hold on, something is happening, wait for thing to finish.
# 200 - 299: Here you go, everything was successful, you got what you expected.
# 300 - 399: You don't have permission to have this thing.
# 400 - 499: You messed up. (404 specifically means we searched for something
#                            that doesn't exist)
# 500 - 599: There is a problem on the server we sent a request to. For example,
#            the server may be down, the website may be down, or other issue.
# For a mor specific list:
# https://httpstatuses.com/

# Prints just the status code.
print(response.status_code)
# If we make a typo in the API Endpoint, we will get a status code of 404

# If we get a status code of 200, we were successful

# If the request fails or is not successful:
# response = requests.get(url="http://api.open-notify.org/iss-now.json")
if response.status_code != 200:
    # In most, if not all cases, it doesn't make sense to just print "Error"
    print("Error")
    # In most cases we may want to raise an exception instead. Although,
    # it's still not a good idea because here we are raising a very general
    # Exception and all for a possibility of not getting a response code of 200:
    ## raise Exception("Bad response from ISS API")

# We could raise an Exception for response code, but there are too many.
# The best way is to use the requests module to generate the Exception instead.
# We can do this with:
response.raise_for_status()


# Getting hold of the actual data from the API:
data = response.json()
print(data)
# Since the data is returned in a JSON format, we can treat it like a Python
# dictionary.
print(data["timestamp"])
print(data["iss_position"])
print(f"Latitude: {data['iss_position']['latitude']}, "
      f"Longitude: {data['iss_position']['longitude']}")
print(data["message"])
# We can also put all the above in their own variables as well.










