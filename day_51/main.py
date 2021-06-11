from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os
from dotenv import load_dotenv

PROMISED_DOWN = 150
PROMISED_UP = 10
CHROME_DRIVER_PATH = "C:\Development\chromedriver.exe"

load_dotenv()
TWITTER_EMAIL = os.getenv("TWITTER_EMAIL")
TWITTER_USERNAME = os.getenv("TWITTER_USERNAME")
TWITTER_PASSWORD = os.getenv("TWITTER_PASSWORD")


class InternetSpeedTwitterBot:

    def __init__(self, driver_path):
        self.driver = webdriver.Chrome(executable_path=driver_path)
        self.up = 0
        self.down = 0

    def get_internet_speed(self):
        """"""
        self.driver.maximize_window()
        time.sleep(2)

        self.driver.get("https://www.speedtest.net/")
        time.sleep(5)

        cookie_consent_button = self.driver.find_element_by_class_name("evidon-barrier-acceptbutton").click()
        time.sleep(2)

        go_button = self.driver.find_element_by_class_name("start-button").click()
        time.sleep(65)

        self.up = self.driver.find_element_by_class_name("upload-speed").text
        print(self.up)

        self.down = self.driver.find_element_by_class_name("download-speed").text
        print(self.down)

        time.sleep(2)

        # self.driver.close()

        # May not need return statement
        return self.up, self.down

    def tweet_at_provider(self):
        """"""
        # self.driver.maximize_window()
        time.sleep(2)

        self.driver.get("https://twitter.com/")

        time.sleep(3)

        # Home page log in button
        self.driver.find_element_by_css_selector("a[data-testid='loginButton']").click()

        time.sleep(2)

        # Email input field
        user = self.driver.find_element_by_name("session[username_or_email]").send_keys(TWITTER_USERNAME)
        time.sleep(2)

        # Password input field
        password = self.driver.find_element_by_name("session[password]").send_keys(TWITTER_PASSWORD + Keys.ENTER)

        time.sleep(2)

        tweet_message = f"Hey Internet Provider, why is my internet speed {self.down}/{self.up} when I pay for " \
                        f"{PROMISED_DOWN}/{PROMISED_UP}? #100DaysOfCode #Python #AngelaYu #LondonAppBrewery #Udemy "
        compose_tweet = self.driver.find_element_by_css_selector("br[data-text='true']").send_keys(tweet_message)
        time.sleep(5)

        tweet_button = self.driver.find_element_by_css_selector("div[data-testid='tweetButtonInline']").click()

        time.sleep(5)

        self.driver.close()


if __name__ == "__main__":
    speed_check = InternetSpeedTwitterBot(CHROME_DRIVER_PATH)
    speed_check.get_internet_speed()
    speed_check.tweet_at_provider()
