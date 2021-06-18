import os
import requests
import time
from dotenv import load_dotenv
from bs4 import BeautifulSoup
from selenium import webdriver

# Section: Env Variables & Global Variables -----------------------------------------------------------------------------------
load_dotenv()
GOOGLE_FORM = os.getenv("RENTING_GOOGLE_FORM")

# Section: BeautifulSoup ---------------------------------------------------------------------
zillo_url = "https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B%22mapBounds%22%3A%7B%22west%22%3A-124.5921424765625%2C%22east%22%3A-120.2745155234375%2C%22south%22%3A36.49088721457784%2C%22north%22%3A39.03776367398378%7D%2C%22mapZoom%22%3A8%2C%22isMapVisible%22%3Afalse%2C%22filterState%22%3A%7B%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%2C%22pmf%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22pf%22%3A%7B%22value%22%3Afalse%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%7D"

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
}

response = requests.get(zillo_url, headers=header)
response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")

# Links for listings
listings_links_list = []
listings_links = soup.find_all(name="a", class_="list-card-link")
for link_tag in listings_links:
    link = link_tag["href"]
    if "http" not in link:
        link = f"https://www.zillow.com{link}"
    if link not in listings_links_list:
        listings_links_list.append(link)
print(listings_links_list)
print(len(listings_links_list))

# Prices for listings
listings_prices_list = []
listings_prices = soup.find_all(name="div", class_="list-card-price")
for price in listings_prices:
    listings_prices_list.append(price.getText())
print(listings_prices_list)
print(len(listings_prices_list))

# Addresses for listings
listings_addresses_list = []
listings_addresses = soup.find_all(name="address", class_="list-card-addr")
for address in listings_addresses:
    listings_addresses_list.append(address.getText())
print(listings_addresses_list)
print(len(listings_addresses_list))

# Section: Selenium ---------------------------------------------------------------------------------
CHROME_DRIVER_PATH = "C:\Development\chromedriver.exe"
driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)

driver.maximize_window()
time.sleep(3)
driver.get(GOOGLE_FORM)
time.sleep(3)

for listing in range(len(listings_links_list)):
    address_of_property_input = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    address_of_property_input.send_keys(listings_addresses_list[listing])
    time.sleep(1)

    price_of_rent_input = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price_of_rent_input.send_keys(listings_prices_list[listing])
    time.sleep(1)

    property_link_input = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    property_link_input.send_keys(listings_links_list[listing])
    time.sleep(1)

    submit_button = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div/span').click()
    time.sleep(3)

    submit_another_response_anchor = driver.find_element_by_tag_name("a")
    if submit_another_response_anchor.text == "Submit another response":
        submit_another_response_anchor.click()

time.sleep(10)
driver.close()
