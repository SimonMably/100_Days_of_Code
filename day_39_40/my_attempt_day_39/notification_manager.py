from dotenv import load_dotenv
import os
import smtplib as smtp

class NotificationManager:
    # This class is responsible for sending notifications with the deal
    # flight details.
    def __init__(self):

        load_dotenv()
        self.EMAIL = os.getenv("PASSWORD")
        self.PASSWORD = os.getenv("PASSWORD")

    def notify_by_email(self, message):
        """Program sends user an e-mail regarding each flight."""

        # TODO: Message will go here.
        message = "Price: "
        # Price
        #
        # Departure City Name
        #
        # Departure Airport IATA Code
        #
        # Arrival City Name
        #
        # Arrival Airport IATA Code
        #
        # Outbound Date
        #
        # Inbound Date

        with smtp.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=self.EMAIL, password=self.PASSWORD)

        connection.sendmail(from_addr=self.EMAIL, to_addrs=self.EMAIL,
                            msg=f"Subject:Flight Deals\n\n{message}")

    def notify_by_sms(self):
        """Program sends user an sms text message regarding each flight.
        MAY COMPLETE FUNCTION AT A LATER DATE."""
        # TODO: Complete function.
        pass













