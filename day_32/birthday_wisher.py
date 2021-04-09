import smtplib as smtp
import datetime as dt
import random
import pandas
import os
from dotenv import load_dotenv

# Environment Variables
load_dotenv()
SENDER = os.getenv("SENDER")
PASSWORD = os.getenv("PASSWORD")

now = dt.datetime.now()
today = (now.month, now.day)

data = pandas.read_csv("birthdays.csv")

birthday_dict = {(data_row['month'], data_row['day']): data_row for
                 index, data_row in data.iterrows()}

if today in birthday_dict:
    birthday_person = birthday_dict[today]
    letter_files = ["letter_1.txt", "letter_2.txt", "letter_3.txt"]

    with open(f"letter_templates/{random.choice(letter_files)}") as f:
        contents = f.read()
        contents = contents.replace("[NAME]", birthday_person["name"])
        print(contents)

    with smtp.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=SENDER, password=PASSWORD)
        connection.sendmail(from_addr=SENDER, to_addrs=SENDER,
                            msg=f"Subject:Happy Birthday\n\n{contents}")

# My Attempt (DOES NOT WORK PROPERLY):
# if today in birthday_dict:
#     birthday_person = birthday_dict[today]
#     letters = ['letter_1.txt', 'letter_2.txt', 'letter_3.txt']
#     with smtp.SMTP("smtp.gmail.com") as connection:
#         connection.starttls()
#         connection.login(user=SENDER, password=PASSWORD)
#
#         with open(f"letter_templates/{random.choice(letters)}", "r") as f:
#             letter = f.readlines()
#             # letter.replace("[NAME]", birthday_person["name"])
#             for line in letter:
#                 line = line.strip()
#                 if "[NAME]" in line:
#                     line = line.replace("[NAME]", birthday_person["name"])
#                 print(line)
#                 connection.sendmail(from_addr=SENDER, to_addrs=SENDER,
#                                   msg=f"Subject:Happy Birthday\n\n{line}")
