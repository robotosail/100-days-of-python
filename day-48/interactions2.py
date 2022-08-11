from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

url = "http://secure-retreat-92358.herokuapp.com/"
chrome_driver_path = "C:/Users/droju/OneDrive/Desktop/100-days-of-python/day-48/dev/chromedriver.exe"
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)


driver.get(url=url)
first_name_input = driver.find_element(By.NAME, "fName")
last_name_input = driver.find_element(By.NAME, "lName")
email_input = driver.find_element(By.NAME, "email")

first_name_input.send_keys("Dave")
first_name_input.send_keys(Keys.TAB)

last_name_input.send_keys("Roger")
last_name_input.send_keys(Keys.TAB)

email_input.send_keys("Dave@test.com")
email_input.send_keys(Keys.ENTER)

driver.quit()
