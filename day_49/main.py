from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import time
import os
from dotenv import load_dotenv

load_dotenv()
EMAIL = os.getenv("EMAIL")
INDEED_PASSWORD = os.getenv("INDEED_PASSWORD")
LINKEDIN_PASSWORD = os.getenv("LINKEDIN_PASSWORD")
LOCATION = os.getenv("LOCATION")

chrome_driver_path = "C:\Development\chromedriver.exe"

driver = webdriver.Chrome(executable_path=chrome_driver_path)



def wait_for_loaded_page():
    """"""
    time.sleep(5)


def go_to_indeed():
    """"""
    driver.get("https://uk.indeed.com/")
    wait_for_loaded_page()


def get_jobs_on_indeed():
    """"""
    indeed_sign_in = driver.find_element_by_link_text("Sign in").click()
    wait_for_loaded_page()

    email_field = driver.find_element_by_name("__email").send_keys(EMAIL)

    password_field = driver.find_element_by_name("__password").send_keys(INDEED_PASSWORD)

    submit_sign_in = driver.find_element_by_id("login-submit-button").click()
    wait_for_loaded_page()
    what_field = driver.find_element_by_name("q").send_keys("Python Developer")

    where_field = driver.find_element_by_name("l").send_keys(LOCATION)

    find_jobs = driver.find_element_by_class_name("icl-WhatWhere-button").click()

    distance_menu = driver.find_element_by_css_selector('#filter-distance > button').click()

    with_five_miles = driver.find_element_by_css_selector("#filter-distance-menu > li:nth-child(1) > a > span").click()


def go_to_linkedin():
    """"""
    link = "https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=102257491&keywords=python%20developer&location=London%2C%20England%2C%20United%20Kingdom&redirect=false&position=1&pageNum=0"
    driver.get(link)
    wait_for_loaded_page()


def get_jobs_on_linkedin():
    """"""
    sign_in_button = driver.find_element_by_link_text("Sign in")
    sign_in_button.click()

    wait_for_loaded_page()
    email_field = driver.find_element_by_id("username")
    email_field.send_keys(EMAIL)
    password_field = driver.find_element_by_id("password")
    password_field.send_keys(LINKEDIN_PASSWORD)
    password_field.send_keys(Keys.ENTER)

    wait_for_loaded_page()

    all_listings = driver.find_elements_by_css_selector(".job-card-container--clickable")

    for listing in all_listings:
        print("called")
        listing.click()
        wait_for_loaded_page()

        #Try to locate the apply button, if can't locate then skip the job.
        try:
            apply_button = driver.find_element_by_css_selector(".jobs-s-apply button")
            apply_button.click()
            wait_for_loaded_page()
            
            #If phone field is empty, then fill your phone number.
            phone = driver.find_element_by_class_name("fb-single-line-text__input")
            if phone.text == "":
                phone.send_keys(PHONE)

            submit_button = driver.find_element_by_css_selector("footer button")

            #If the submit_button is a "Next" button, then this is a multi-step application, so skip.
            if submit_button.get_attribute("data-control-name") == "continue_unify":
                close_button = driver.find_element_by_class_name("artdeco-modal__dismiss")
                close_button.click()
                wait_for_loaded_page()
                discard_button = driver.find_elements_by_class_name("artdeco-modal__confirm-dialog-btn")[1]
                discard_button.click()
                print("Complex application, skipped.")
                continue
            else:
                submit_button.click()
        
            #Once application completed, close the pop-up window.
            wait_for_loaded_page()
            close_button = driver.find_element_by_class_name("artdeco-modal__dismiss")
            close_button.click()

        #If already applied to job or job is no longer accepting applications, then skip.
        except NoSuchElementException:
            print("No application button, skipped.")
            continue

    wait_for_loaded_page()
    driver.quit()


which_jobsite = input("Where would you like to search? Indeed or LinkedIn: ").title()
if which_jobsite == "indeed":
    go_to_indeed()
    get_jobs_on_indeed()
elif which_jobsite == "LinkedIn" or which_jobsite == "linkedin" or which_jobsite == "linkedIn":
    go_to_linkedin()
    get_jobs_on_linkedin()

