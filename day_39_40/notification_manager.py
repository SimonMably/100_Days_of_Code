from twilio.rest import Client
from dotenv import load_dotenv
import os
import smtplib


load_dotenv()

TWILIO_SID = os.getenv("SID")
TWILIO_AUTH_TOKEN = os.getenv("AUTH_TOKEN")
TWILIO_VIRTUAL_NUMBER = os.getenv("VIRTUAL_NUMBER")
TWILIO_VERIFIED_NUMBER = os.getenv("VERIFIED_NUMBER")
SENDER = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")


class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        """Sends a notification of flight deal via text message."""
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        # Prints if successfully sent.
        print(message.sid)

    def send_emails(self, emails, message, google_flight_link):
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(SENDER, PASSWORD)
            for email in emails:
                connection.sendmail(
                    from_addr=SENDER,
                    to_addrs=email,
                    msg=f"Subject:New Low Price Flight!\n\n{message}\n"
                        f"{google_flight_link}".encode('utf-8'))
