import os
from dotenv import load_dotenv
import time
import requests


load_dotenv()
SHEETY_USER_ENDPOINT = os.getenv("SHEETY_USERS_ENDPOINT")
SHEETY_TOKEN = os.getenv("SHEET_TOKEN")


def clear_screen():
    """Clears the screen of text, if customer_acquisition.py file is run
    using a Terminal program."""
    # for windows
    if os.name == 'nt':
        _ = os.system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = os.system('clear')


def acquire_name_and_email():
    """Takes in user's name and email address as inputs"""
    first_name = input("What is you first name: ")

    last_name = input("What is you last name: ").title()

    email = input("What is your email address: ").title()

    verify_email = input("Verify your email address: ")

    if email == verify_email:
        # print(f"\nYour name is {first_name} {last_name} and your email "
        #       f"address is {email}\n")
        # TODO: call post_details() here
        post_details(first_name=first_name, last_name=last_name, email=email)
        print("Congratulations. Your details have been added, you are now "
              "apart of the club!")
    else:
        print("\nThe email you provided in both attempts didn't match. "
              "Please try again.\n")
        time.sleep(2)
        clear_screen()
        acquire_name_and_email()


def post_details(first_name, last_name, email):
    """Uses the Sheety API to post user information to Users Google Sheet via
    post request."""
    data = {
        "user": {
            "firstName": first_name,
            "lastName": last_name,
            "email": email,
        }
    }

    header = {
        "Authorization": SHEETY_TOKEN,
    }

    add_data = requests.post(url=SHEETY_USER_ENDPOINT, json=data,
                             headers=header)
    print(add_data.json())
    print(add_data.text)


# ------------------------------------------------------------------------------
print("\nWelcome to Simon's Flight Club.\n"
      "We find the best flight deals and email them to you.\n")

acquire_name_and_email()





