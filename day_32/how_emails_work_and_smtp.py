import smtplib
from dotenv import load_dotenv
import os

# How Emails work behind the scenes:
'''
A user sends an email from their email provider, which will receive the email
in their Mail Server (eg. Gmail Mail Server) and then the email will
be stored in the Mail Server of the recipients email provider until the
recipient log into his/her email account and downloads the email t view.

Example:
Person 1 sends email --> received in Gmail Mail Server -----------------------¬|
recipient logs into email account & views email-- stored in Yahoo Mail Server<--

For emails to go through all of these step, it relies on SMTP (Simple Mail
Transfer Protocol). SMTP contains all of the rules that determine how an
email is received by Mail Servers, passed onto the next Mail Server and how
emails can be sent around the internet.

We can use Python to send emails with the built-in module: smtplib.
'''

# Using the smtplib module:

'''SMTP Information
Gmail: smtp.gmail.com
Hotmail.com: smtp.live.com
Yahoo: smtp.mail.yahoo.com

For other providers, search on Google or other search engine.

'''


# The email address we're going to use to send emails.
# Before the @ sign: Identity of the email account
# After the @ sign: Identity of the email provider
load_dotenv()
my_email = os.getenv("SENDER")
password = os.getenv("PASSWORD")
recipient = os.getenv("RECIPIENT")

# Creating an object with the SMTP() class
# - Specify the location of email providers SMTP server (each email provider
# has their own SMTP server location. eg. for gmail: smtp.gmail.com)
with smtplib.SMTP("smtp.gmail.com") as connection:
    # starttls() = a way of using Transport Layer Security to secure our
    # connection with our email server. Encrypts emails so if someone intercepts
    # them,they can't read the emails.
    connection.starttls()
    # Pass username and password into login() as arguments
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email, to_addrs=recipient,
                        msg="Subject:Hello\n\nThis is the body of this email.")
# connection.close()
# Since we used the 'with' keyword with smtp.SMTP("smtp.gmail.com"), the 'with'
# will automatically close the 'connection'.












