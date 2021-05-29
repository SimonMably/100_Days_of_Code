from selenium import webdriver
from selenium.webdriver.common.keys import Keys


chrome_driver_path = "C:\Development\chromedriver.exe"

driver = webdriver.Chrome(executable_path=chrome_driver_path)

# driver.get("https://en.wikipedia.org/wiki/Main_Page")

# Challenge: Use Selenium to print the total number of articles from the 
# Wikipedia homepage. 

# number_of_articles = driver.find_element_by_id("articlecount")
# number_of_articles = driver.find_element_by_css_selector("#articlecount a")
# number_of_articles.click()

# all_portals = driver.find_element_by_link_text("All portals")
# all_portals.click()

# search = driver.find_element_by_name("search")
# search.send_keys("Python")
# search.send_keys(Keys.ENTER)

# Challenge
driver.get("http://secure-retreat-92358.herokuapp.com/")
first_name = driver.find_element_by_name("fName")
first_name.send_keys("First")

last_name = driver.find_element_by_name("lName")
last_name.send_keys("Last")

email_field = driver.find_element_by_name("email")
email_field.send_keys("test@email.com")

# submit_button = driver.find_element_by_css_selector("form button")
submit_button = driver.find_element_by_class_name("btn-primary")
submit_button.click()


# driver.close()
