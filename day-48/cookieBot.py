from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

url = "http://orteil.dashnet.org/experiments/cookie/"
chrome_driver_path = r"C:/Users/droju/Onedrive/Desktop/100-days-of-python/day-48/dev/chromedriver.exe"
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)

driver.get(url=url)

cookie = driver.find_element(By.ID, "cookie")
time_to_buy = time.time() + 5
stop_time = time.time() + 60 * 10  # 5 min

items = driver.find_elements(By.CSS_SELECTOR, "#store div")
# getting the id of each item
item_ids = [item.get_attribute("id") for item in items]
names = []

gameon = True
while gameon:
    cookie.click()
    # checking if it is time to buy upgrades
    if time.time() > time_to_buy:
        prices = []
        # getting the items available for purchase
        store = driver.find_elements(By.CSS_SELECTOR, "#store b")
        # getting the amount of money we have
        money = driver.find_element(By.ID, "money").text
        if "," in money:
            money = money.replace(",", "")
        money = int(money)

        # looping through the number of items in the store
        for item in range(len(store) - 1):
            # getting hold of each item
            item = store[item]
            # splitting the text from the - sign then removing any whitespaces and commas
            itemprice = int(item.text.split(
                "-")[1].strip().replace(",", ""))
            # adding items to the corresponding list
            prices.append(itemprice)

        # creating a dictionary to store the price of an item and its id
        upgrades = {}
        for n in range(len(prices)):
            upgrades[prices[n]] = item_ids[n]

       # Find upgrades that we can currently afford
        affordable_upgrades = {}
        for cost, id in upgrades.items():
            if money > cost:
                affordable_upgrades[cost] = id

        # finding the most expensive upgrade using the max function
        highest_price_affordable_upgrade = max(affordable_upgrades)
        print(highest_price_affordable_upgrade)
        # getting the id of the most expensive upgrade
        to_purchase_id = affordable_upgrades[highest_price_affordable_upgrade]

        # Purchase the most expensive affordable upgrade
        driver.find_element(By.ID, to_purchase_id).click()

        # Add another 5 seconds until the next check
        time_to_buy = time.time() + 10

    # stopping the game after 5 min
    if time.time() > stop_time:
        cookie_per_s = driver.find_element(By.ID, "cps").text
        print(cookie_per_s)
        break
