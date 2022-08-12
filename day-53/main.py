import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import requests

chrome_driver_path = r"C:/Users/droju/Onedrive/Desktop/100-days-of-python/day-48/dev/chromedriver.exe"
google_form_link = "https://docs.google.com/forms/d/e/1FAIpQLSfwofMX-to4tYUsxR9wFyeLTroM6afgPZufCbNxet-uLlSrJA/viewform?usp=sf_link"
rental_addr = "https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A%7B%22west%22%3A-122.68662335820738%2C%22east%22%3A-122.17987897344176%2C%22south%22%3A37.60951903667279%2C%22north%22%3A37.94113068145618%7D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A11%7D"
service = Service(chrome_driver_path)

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.81 Safari/537.36 Edg/104.0.1293.47",
    "Accept-Language": "en-US,en;q=0.9"
}

# requesting for the page
response = requests.get(rental_addr, headers=headers).text
# sending the requested page to beautiful soup and getting the html
soup = BeautifulSoup(response, "html.parser")

# getting hold of all the property links
listing_links = soup.select(".property-card-link")
links = []

# adding the full url to all the links that don't have the full url
for link in listing_links:
    href = link["href"]
    if "http" not in href:
        links.append(f"https://www.zillow.com{href}")
    else:
        links.append(href)

# getting hold of the address and storing it into a list using beautiful soup
listting_addr = soup.select("[data-test='property-card-addr']")
addrs = [address.get_text().split(" | ")[-1]
         for address in listting_addr]

# getting hold of the house prices and storing it into a list using beautiful soup
listing_prices = soup.select("[data-test='property-card-price']")
prices = [price.get_text().split("+")[0]
          for price in listing_prices if "$" in price.text]

# initializing the browser
driver = webdriver.Chrome(service=service)


def fillForm():
    for n in range(len(links)):
        # opening the desired form link
        driver.get(url=google_form_link)
        # pausing script so the page loads
        time.sleep(2)
        # getting the input elements
        addr = driver.find_element(
            By.CSS_SELECTOR, "#mG61Hd > div.RH5hzf.RLS9Fe > div > div.o3Dpx > div:nth-child(1) > div > div > div.AgroKb > div > div.aCsJod.oJeWuf > div > div.Xb9hP > input")

        price = driver.find_element(
            By.CSS_SELECTOR, "#mG61Hd > div.RH5hzf.RLS9Fe > div > div.o3Dpx > div:nth-child(2) > div > div > div.AgroKb > div > div.aCsJod.oJeWuf > div > div.Xb9hP > input")
        link = driver.find_element(
            By.CSS_SELECTOR, "#mG61Hd > div.RH5hzf.RLS9Fe > div > div.o3Dpx > div:nth-child(3) > div > div > div.AgroKb > div > div.aCsJod.oJeWuf > div > div.Xb9hP > input")
        # getting the submit button element
        submit = driver.find_element(
            By.CSS_SELECTOR, "#mG61Hd > div.RH5hzf.RLS9Fe > div > div.ThHDze > div.DE3NNc.CekdCb > div.lRwqcd > div")

        # filling in the form with the corresponding value
        addr.send_keys(addrs[n])
        # pausing the script in between so it doesn't go too fast
        time.sleep(2)
        price.send_keys(prices[n])
        # pausing the script in between so it doesn't go too fast
        time.sleep(2)
        link.send_keys(links[n])
        # pausing the script in between so it doesn't go too fast
        time.sleep(2)
        # clicking the submit button on every successufully filled form
        submit.click()


fillForm()
