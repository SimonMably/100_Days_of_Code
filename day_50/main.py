from selenium import webdriver
from selenium.common.exceptions import StaleElementReferenceException, ElementClickInterceptedException
import time
import os
from dotenv import load_dotenv

load_dotenv()
EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")

chrome_driver_path = "C:\Development\chromedriver.exe"

driver = webdriver.Chrome(executable_path=chrome_driver_path)


def wait_for_elements_to_load(sec):
    """Used as a delay until web page elements have loaded."""
    time.sleep(sec)


def login_tinder():
    """Login to the Tinder site."""
    driver.maximize_window()
    driver.get("https://tinder.com/")
    wait_for_elements_to_load(5)

    login_page_spans = driver.find_elements_by_tag_name("span")
    for span in login_page_spans:
        if span.text == "LOG IN":
            span.click()

    wait_for_elements_to_load(5)

    login_with_facebook()


def login_with_facebook():
    """Login to Tinder with Facebook account."""
    wait_for_elements_to_load(5)
    login_via_accounts_buttons = driver.find_elements_by_tag_name("span")

    for button in login_via_accounts_buttons:
        if button.text == "LOGIN WITH FACEBOOK":
            button.click()

    wait_for_elements_to_load(15)

    # Switching between windows
    base_window = driver.window_handles[0]
    fb_login_window = driver.window_handles[1]

    driver.switch_to.window(fb_login_window)

    wait_for_elements_to_load(10)

    # Clicks "Accept All" on cookie prompt
    cookie_buttons = driver.find_elements_by_tag_name("button")
    for button in cookie_buttons:
        if button.text == "Accept All":
            button.click()

    email_field = driver.find_element_by_id("email").send_keys(EMAIL)
    password_field = driver.find_element_by_id("pass").send_keys(PASSWORD)
    wait_for_elements_to_load(1)
    login_button = driver.find_element_by_name("login").click()

    # Switch back to previous window
    driver.switch_to.window(base_window)

    wait_for_elements_to_load(7)

    dismiss_request_pop_ups()


def dismiss_request_pop_ups():
    """Clicks relevant buttons to dismisses pop-up notifications and such for cookies and location."""

    tinder_page_spans = driver.find_elements_by_tag_name("span")
    for span in tinder_page_spans:
        # For location
        try:
            if span.text == "ALLOW":
                span.click()
        except StaleElementReferenceException as e:
            print("Pass on StaleElementReferenceException")

    wait_for_elements_to_load(5)

    tinder_page_spans = driver.find_elements_by_tag_name("span")
    for span in tinder_page_spans:
        # Notifications for new matches and messages
        if span.text == "NOT INTERESTED":
            span.click()

    wait_for_elements_to_load(5)

    tinder_page_buttons = driver.find_elements_by_tag_name("button")
    for button in tinder_page_buttons:
        # Accept cookies button
        if button.text == "I ACCEPT":
            button.click()

    wait_for_elements_to_load(5)

    nope()


def nope():
    """Clicks on 'NOPE' button. Equivalent to swiping left."""
    tinder_buttons = driver.find_elements_by_tag_name("button")

    for button in tinder_buttons:
        # print(button.text)
        for _ in range(99):
            try:
                if button.text == "NOPE":
                    button.click()
                    wait_for_elements_to_load(10)
            except ElementClickInterceptedException:
                add_home_dismiss = driver.find_element_by_css_selector(
                    '#o-441539182 > div > div > div.Pt\(12px\).Pb\(8px\).Px\(36px\).Px\(24px\)--s > button.button.Lts\(\$ls-s\).Z\(0\).CenterAlign.Mx\(a\).Cur\(p\).Tt\(u\).Ell.Bdrs\(100px\).Px\(24px\).Px\(20px\)--s.Py\(0\).Mih\(42px\)--s.Mih\(50px\)--ml.C\(\$c-secondary\).C\(\$c-base\)\:h.Fw\(\$semibold\).focus-button-style.D\(b\).Mx\(a\) > span')
                add_home_dismiss.click()
                continue


def like():
    """Clicks on 'LIKE' button. Equivalent to swiping right."""
    # HAS NOT BEEN TESTED
    tinder_buttons = driver.find_elements_by_tag_name("button")
    for button in tinder_buttons:
        if button.text == "LIKE":
            for _ in range(10):
                button.click()
                wait_for_elements_to_load(3)


login_tinder()
