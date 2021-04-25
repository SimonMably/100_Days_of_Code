import requests
import os
from datetime import datetime as dt
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("PIXELA_TOKEN")
USERNAME = os.getenv("PIXELA_USERNAME")

graph_name = "graph1"
# day = None

pixela_endpoint = "https://pixe.la/v1/users"

# -----------------------------------------------------------------------------
# Creating an account with Pixela
user_parameters = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_parameters)
# print(response.text)
# -----------------------------------------------------------------------------
# Creating a Pixe.la Graph
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_parameters = {
    "id": graph_name,
    "name": "Programming Graph",
    "unit": "Hours",
    "type": "float",
    "color": "sora",
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_parameters,
#                          headers=headers)
# print(response.text)

# -----------------------------------------------------------------------------
graph_link = "https://pixe.la/v1/users/simrusmab/graphs/graph1.html"

print("Welcome to the 'Habit Tracker'.\n"
      f"Go to {graph_link} to view the graph.\n")

print("You can input data for TODAY, UPDATE or DELETE existing data.")

user_input = input("What would you like to do? (Enter: INPUT, UPDATE, or "
                   "DELETE): ").upper()

# TODO: Complete
if user_input == "INPUT":
    today = dt.now()
    formatted_date = today.strftime("%Y%m%d")
    # print(formatted_date)

    blue_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{graph_name}"

    # Post graph data for today
    pixel_parameters = {
        "date": formatted_date,
        "quantity": input("\nHow many hours did you study today? "),
    }

    response = requests.post(url=blue_pixel_endpoint, json=pixel_parameters,
                             headers=headers)
    print(response.text)

elif user_input == "UPDATE":
    print("\nProvide new total time to overwrite time for an existing post")

    date = input("\nGive the date you wish to update. dd/mm/yyyy: ").split("/")

    redo_hours = input("\nNew total time: ")

    day = dt(year=int(date[2]), month=int(date[1]), day=int(date[0]))

    update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{graph_name}/" \
                      f"{day.strftime('%Y%m%d')}"

    update_parameters = {
        "quantity": redo_hours,
    }

    response = requests.put(url=update_endpoint, json=update_parameters,
                            headers=headers)
    print(response.text)

elif user_input == "DELETE":
    day = dt(year=2021, month=4, day=23)
    delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{graph_name}/" \
                      f"{day.strftime('%Y%m%d')}"

    response = requests.delete(url=delete_endpoint, headers=headers)
    print(response.text)
else:
    print("Please enter 'INPUT', 'UPDATE', or 'DELETE'")

# -----------------------------------------------------------------------------
# Filling up the graph


# Update previously created graph data


# Deleting posted graph data
