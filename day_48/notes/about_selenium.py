from selenium import webdriver

chrome_driver_path = "C:\Development\chromedriver.exe"

driver = webdriver.Chrome(executable_path=chrome_driver_path)

# Will open website in a new browser window
# driver.get("https://www.amazon.co.uk/Clean-Code-Handbook-Software-Craftsmanship/dp/0132350882/ref=lp_269678_1_11")
# price = driver.find_element_by_id("price")
# print(price.text)

# Finding an HTML element by name (commonly used with Selenium)
# driver.get("https://www.python.org/")
# search_bar = driver.find_element_by_name("q")
# print(search_bar.tag_name)

# Finding an HTML element by Class name
# driver.get("https://www.python.org/")
# logo = driver.find_element_by_class_name("python-logo")
# print(logo.size)

# Finding an HTML element by CSS Selector
# driver.get("https://www.python.org/")
# documentation_link = driver.find_element_by_css_selector(".documentation-widget a")
# print(documentation_link.text)

# Finding an HTML element by XPath
# driver.get("https://www.python.org/")
# bug_link = driver.find_element_by_xpath('//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
# print(bug_link.text)


# Finding multiple instances of an elements
# eg. driver.find_elements_by_css_selector()

# Closes the browser tab that opened with 'driver.get()'
driver.close()

# Closes the entire browser
# driver.quit()
