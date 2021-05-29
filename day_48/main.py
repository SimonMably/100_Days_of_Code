from selenium import webdriver
import time

chrome_driver_path = "C:\Development\chromedriver.exe"

driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("http://orteil.dashnet.org/experiments/cookie/")

# timeout = time.time() + 5

cookie = driver.find_element_by_id("cookie")

items = driver.find_elements_by_css_selector("#store div")
item_ids = [item.get_attribute("id") for item in items]

timeout = time.time() + 5
five_min = time.time() + 60 * 5

while True:
    cookie.click()

    if time.time() > timeout:
        # time.sleep(1)
        # timeout = time.time() + 5

        prices = driver.find_elements_by_css_selector("#store b")
        item_prices = []
        
        for price in prices:
            price_text = price.text
            if price_text != "":
                cost = int(price_text.split("-")[1].strip().replace(",", ""))
                item_prices.append(cost)

        cookie_upgrades = {}
        for n in range(len(item_prices)):
            cookie_upgrades[item_prices[n]] = item_ids[n]

        currency = driver.find_element_by_id("money").text
        if "," in currency:
            currency = currency.replace(",", "")
        cookie_count = int(currency)

        affordable_upgrades = {}
        for cost, id in cookie_upgrades.items():
            if cookie_count > cost:
                 affordable_upgrades[cost] = id

        highest_price_affordable_upgrade = max(affordable_upgrades)
        print(highest_price_affordable_upgrade)
        to_purchase_id = affordable_upgrades[highest_price_affordable_upgrade]

        driver.find_element_by_id(to_purchase_id).click()
        
        timeout = time.time() + 5

    # if time.time() > five_min:
    #     cookie_per_s = driver.find_element_by_id("cps").text
    #     print(cookie_per_s)
    #     break
