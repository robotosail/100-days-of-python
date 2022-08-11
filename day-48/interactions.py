
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
# importing keys on a keyboard that can be pressed
from selenium.webdriver.common.keys import Keys

url = "https://en.wikipedia.org/wiki/Main_Page"
chrome_driver_path = "C:/Users/droju/OneDrive/Desktop/100-days-of-python/day-48/dev/chromedriver.exe"
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)

# opening the browser
driver.get(url=url)

# article_count = driver.find_element(
#     by=By.CSS_SELECTOR, value="#articlecount a")
# article_count.click()  # clicking on the element

# # clicks on a link elemnent with a text of all portals
# contents = driver.find_element(by=By.LINK_TEXT, value="Contents")
# contents.click()

# typing into input fields
search = driver.find_element(by=By.NAME, value="search")
search.send_keys("Python")
# pressing the enter key
search.send_keys(Keys.ENTER)

# closing the page
# driver.quit()
