# https://www.ebay.com/itm/363933612994?_trkparms=amclksrc%3DITM%26aid%3D1110018%26algo%3DHOMESPLICE.COMPLISTINGS%26ao%3D1%26asc%3D20210609144404%26meid%3D6f47f0fa72434841a3ce9686d810c386%26pid%3D101196%26rk%3D10%26rkt%3D12%26sd%3D373990928169%26itm%3D363933612994%26pmt%3D1%26noa%3D0%26pg%3D2047675%26algv%3DItemStripV101HighAdFeeWithCompV3RankerWithKnnRecallV1%26brand%3DJordan&_trksid=p2047675.c101196.m2219&amdata=cksum%3A3639336129946f47f0fa72434841a3ce9686d810c386%7Cenc%3AAQAHAAABEA%252FJiT7ssNXrEsx1zZncFUUkLU8ikMh%252FiWOsxkTqeqIbE5K4lpcDSKjAfQ%252F1if83xaZVNs5dLYPZjg0g7Mr9JEYFSP1ni6p4oGZWa3NXR3vdcOmILvtLAY8FEwWWTydBO32TyVnpG4rGr2Sspd7r4YjecSSJaC63F2q5GCpGOLhpbR4u4BxHEdGdLOXMNzsVHsZPl4sIwJcMjrW32e4ghrHtMjW%252F6aB7mjTLNNgyyC7OnbU5OUDXjVBbWgyHUHeHg6Sg%252FavfwquNafKsswMMxGd%252BF8VCnAimCnmYWahAL4mngf9qORJipLvowp7DsQfYemXS4926MXdKRwEhjWuQPsdSnHzC%252BM9PG8XT2QsapyMV%7Campid%3APL_CLK%7Cclp%3A2047675&epid=19052854548

# importing selenium w
from selenium import webdriver
# needed inorder to use the driver
from selenium.webdriver.chrome.service import Service
# needed in order to get elements
from selenium.webdriver.common.by import By

# the path for chrome webdriver
chrome_driver_path = r"C:\Users\droju\OneDrive\Desktop\100-days-of-python\day-48\dev\chromedriver.exe"
url = "https://www.amazon.com/Jordan-Mens-Retro-CT8013-Playoffs/dp/B09KX3MRPQ/ref=sr_1_1?crid=3RTSB4NE73KNS&keywords=jordan%2B12%2Bshoes&qid=1660156456&s=apparel&sprefix=%2Cfashion-mens%2C44&sr=1-1&th=1&psc=1"
# initializing the webdriver for chrome browser
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)

# opens up a webpage with a url
driver.get(url=url)

# # closes the tab
# driver.close()

# getting an element from the webpage by the id
element = driver.find_element(by=By.ID, value="productTitle")

# # prints the value in the element
# print(element.text)

# # gets the id of the element
# print(element.get_attribute("id"))

# # gets the element using the class name
# element.find_element(by=By.CLASS_NAME, value="a-price-whole")

# getting an element by its xpath - to find the xpath of an element inspect the element then right click on it and click copy xpath
# xpath = driver.find_element(
#     by=By.XPATH, value='//*[@id="corePriceDisplay_desktop_feature_div"]/div[1]/span/span[2]/span[2]')
# print(xpath.text)

# # get multiple elements
# driver.find_elements(by=By.CSS_SELECTOR, value="")

# closes the whole browser and quits the program
driver.quit()
