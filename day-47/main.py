#----------Amazon Price Tracker-------------#
# importing request module
import requests
from bs4 import BeautifulSoup
import lxml
import smtplib
import os
# the product url
product_url = "https://www.amazon.com/Jordan-Mens-Retro-CT8013-Playoffs/dp/B09KX3MRPQ/ref=sr_1_1?crid=3RTSB4NE73KNS&keywords=jordan%2B12%2Bshoes&qid=1660156456&s=apparel&sprefix=%2Cfashion-mens%2C44&sr=1-1&th=1&psc=1"

# url headers
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.81 Safari/537.36 Edg/104.0.1293.47",
    "Accept-Language": "en-US,en;q=0.9"
}
# storing the data into a variable
response = requests.get(url=product_url, headers=headers)
# initializing beautiful soup
soup = BeautifulSoup(markup=response.text, features="lxml")

# finding the price of the product
product_title = soup.find(name="span", id="productTitle").getText().strip()
product_price_whole = soup.find(name="span", class_="a-price-whole").getText()
product_price_cent = soup.find(
    name="span", class_="a-price-fraction").getText()
# combining the whole price and the cents together
product_price = float(product_price_whole + product_price_cent)

user_name = os.getenv("USR")
pwd = os.getenv("PWD")

if product_price < 187:
    with smtplib.SMTP(host="smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=user_name, password=pwd)
        connection.sendmail(from_addr=user_name, to_addrs=user_name,
                            msg=f"Subject: Amazon Price Alert\n\n{product_title} is now {product_price}. Be fast and get it now! \nclick here to view: {product_url}")
