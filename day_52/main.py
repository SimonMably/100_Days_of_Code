from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
from selenium.webdriver.common.keys import Keys
import time
import os
from dotenv import load_dotenv

# Username and Password variables from .env file goe here
load_dotenv()
EMAIL = os.getenv("EMAIL")
USERNAME = os.getenv("USERNAME")
PASSWORD = os.getenv("PASSWORD")
CHROME_DRIVER_PATH = "C:\Development\chromedriver.exe"
SIMILAR_ACCOUNT = os.getenv("SIMILAR_ACCOUNT")


class InstaFollower:
    """Uses Selenium as an automated Instagram bot to log into Instagram, go to a particular account (SIMILAR_ACCOUNT),
    scrolls through their followers list and clicks on the 'Follow' button next to each of their followers."""

    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)

    def login(self):
        """Logs into Instagram and clicks on relevant button regarding saving login information and turning on notification
        prompts."""
        self.driver.maximize_window()
        time.sleep(2)
        
        self.driver.get("https://www.instagram.com/accounts/login/")
        time.sleep(5)

        accept_cookies_xpath = '/html/body/div[3]/div/div/button[1]'
        accept_cookies = self.driver.find_element_by_xpath(accept_cookies_xpath).click()
        time.sleep(10)

        username_input = self.driver.find_element_by_name("username").send_keys(EMAIL)

        password_input = self.driver.find_element_by_name("password").send_keys(PASSWORD + Keys.ENTER)
        time.sleep(5)

        # Save Login Information Prompt
        save_login_buttons = self.driver.find_elements_by_tag_name("button")
        for button in save_login_buttons:
            if button.text == "Not Now":
                button.click()
        time.sleep(5)

        # Turn On Notification Prompt
        notification_buttons = self.driver.find_elements_by_tag_name("button")
        for button in notification_buttons:
            if button.text == "Not Now":
                button.click()
        time.sleep(10)

    def find_followers(self):
        """Goes to the Instagram account in SIMILAR_ACCOUNT variable, targets their follower count element and scrolls
        through list of followers."""
        self.driver.get(f"https://www.instagram.com/{SIMILAR_ACCOUNT}/")
        time.sleep(3)

        followers_popup = self.driver.find_element_by_css_selector(f"a[href='/{SIMILAR_ACCOUNT}/followers/']").click()
        time.sleep(3)

        followers_list_xpath = '//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a/span'
        followers_list = self.driver.find_element_by_css_selector("div[class='isgrP']")

        for _ in range(50):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", followers_list)
            time.sleep(1)
        time.sleep(10)

    def follow(self):
        """Clicks on the 'Follow' button next to each account in the follower list of account in SIMILAR_ACCOUNT."""
        follow_buttons = self.driver.find_elements_by_tag_name("button")
        for button in follow_buttons:
            if button.text == "Follow":
                button.click()
                time.sleep(2)

        self.driver.close()


if __name__ == "__main__":
    instabot = InstaFollower()
    instabot.login()
    instabot.find_followers()
    instabot.follow()











