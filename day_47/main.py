import os
import requests
from bs4 import BeautifulSoup
import smtplib
from dotenv import load_dotenv
# from pprint import pprint

# --- GET Request for Product Page & Scrape Price ------------------------------

URL = "https://www.amazon.co.uk/Clean-Code-Handbook-Software-Craftsmanship/dp/0132350882/ref=lp_269678_1_11"

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
}

response = requests.get(URL, headers=header)
# amazon_product_page = response.text
soup = BeautifulSoup(response.content, "html.parser")
# print(soup.prettify())

product_title = soup.find(name="span", id="productTitle").getText().strip()
product_price = soup.find(name="span", id="price").getText()
split_price = product_price.split("£")
no_currency_price = float(split_price[1])

# --- Email Alert When Product Price Meets Criteria ----------------------------
load_dotenv()
EMAIL = os.getenv("Y_EMAIL")
PASSWORD = os.getenv("Y_PASSWORD")
RECIPIENT = os.getenv("RECIPIENT")

if no_currency_price <= 31.0:
    message = f"{product_title} is now {product_price}\n{URL}"

    with smtplib.SMTP("smtp.mail.yahoo.com", 465) as connection:
        # connection.ehlo()
        connection.starttls()
        # connection.ehlo()
        connection.login(user=EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=EMAIL, to_addrs=RECIPIENT,
                            msg=f"Subject:Amazon Price Alert - {product_title}\n\n"
                                f"{message}"
                            )
