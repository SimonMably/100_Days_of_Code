import requests

# Open Trivia DataBase API
# <------- Endpoint --------> <---- Parameters ---->
# https://opentdb.com/api.php?amount=10&type=boolean

parameters = {
    "amount": 10,
    "type": "boolean",
    "category": 18,
}

question_response = requests.get("https://opentdb.com/api.php",
                                 params=parameters)
question_response.raise_for_status()
question_data = question_response.json()["results"]
