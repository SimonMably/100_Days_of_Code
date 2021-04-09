import smtplib as smtp
import random as rand
import datetime as dt
import os
from dotenv import load_dotenv

load_dotenv()
sender = os.getenv("SENDER")
password = os.getenv("PASSWORD")
recipient = os.getenv("RECIPIENT")

now = dt.datetime.now()
day_of_week = now.weekday()

if day_of_week == 0:
    with smtp.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=sender, password=password)

        with open("quotes.txt", "r") as f:
            quotes = f.readlines()
            quote = rand.choice(quotes).strip()
            print(quote)

        connection.sendmail(from_addr=sender, to_addrs=sender,
                            msg=f"Subject:Motivational Quote\n\n{quote}")
