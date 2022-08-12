#----------Instagram FollowBot-----------#


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
chrome_driver_path = r"C:/Users/droju/Onedrive/Desktop/100-days-of-python/day-48/dev/chromedriver.exe"
similar_account = "the person you want to follow"
USERNAME = "Your user name"
PASSWORD = "your password"


class InstaFollower:
    def __init__(self) -> None:
        self.service = Service(chrome_driver_path)
        self.driver = webdriver.Chrome(service=self.service)

    def login(self, username, password):
        url = "https://www.instagram.com/accounts/login/"
        self.driver.get(url)

        # pausing the script so the page can fully load
        time.sleep(5)

        # filling in the form
        username_input = self.driver.find_element(
            By.NAME, 'username')
        username_input.send_keys(username)

        # adding a timer so the bot seems more human
        time.sleep(8)

        password_input = self.driver.find_element(
            By.NAME, 'password')
        password_input.send_keys(password)

        # pausing the script
        time.sleep(2)

        submit = self.driver.find_element(
            by=By.CLASS_NAME, value="L3NKy")
        submit.click()

        print("successfully logged in")

    def find_followers(self):
        # change the link to the person to follow
        url = f"https://www.instagram.com/{similar_account}/followers"
        time.sleep(6)
        self.driver.get(url)
        time.sleep(10)

        # getting the scrollable elemnt
        page = self.driver.find_element(
            By.CLASS_NAME, '_aano')

        for i in range(1):
            # the second  first position argument should be the element to be scrolled
            self.driver.execute_script(
                f"arguments[0].scrollTop = arguments[0].scrollHeight", page)
            time.sleep(2)

    def follow(self):
        # getting hold of the follow button
        followbtn = self.driver.find_elements(
            By.CSS_SELECTOR, "._aano div div div button")
        for people in followbtn:
            print(people.text)
            people.click()
            print("followed")
            time.sleep(6)


instaBot = InstaFollower()

instaBot.login(USERNAME, PASSWORD)
instaBot.find_followers()
instaBot.follow()
