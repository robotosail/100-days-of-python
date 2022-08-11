from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_driver_path = r"C:\Users\droju\OneDrive\Desktop\100-days-of-python\day-48\dev\chromedriver.exe"
url = "https://www.python.org/"
service = Service(executable_path=chrome_driver_path)
driver = webdriver.Chrome(service=service)

driver.get(url=url)

event_times = driver.find_elements(
    by=By.CSS_SELECTOR, value=".event-widget time")  # returns a list

event_names = driver.find_elements(
    by=By.CSS_SELECTOR, value=".event-widget li a")

# looping through the length of the event_names: runs 4 times
events = {n: {"time": event_times[n].text, "name": event_names[n].text}
          for n in range(len(event_names))}


print(events)
driver.quit()
