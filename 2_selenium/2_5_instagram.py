# BTK Academy
# Advanced Python Programming From Zero
# Lecture 2.4: Get Instagram Followers with Using Selenium
# python 2_5_instagram.py
blank = "----------------------"

# Get Instagram Followers
from instagram_user_info import username, password
from selenium import webdriver 
from selenium.webdriver.common.by import By
import time


class Instagram:
    def __init__(self, username, password):
        self.browser = webdriver.Edge()
        self.username = username
        self.password = password
        self.followers_link = []

##############################################################################################################

    def sign_in(self):
        self.browser.get("https://www.instagram.com/accounts/login/")
        time.sleep(1)

        username = self.browser.find_element(By.XPATH, "//*[@id='loginForm']/div/div[1]/div/label/input").send_keys(self.username)
        password = self.browser.find_element(By.XPATH, "//*[@id='loginForm']/div/div[2]/div/label/input").send_keys(self.password)
        time.sleep(1)

        # sign in click
        self.browser.find_element(By.XPATH, "//*[@id='loginForm']/div/div[3]").click()
        time.sleep(5)

        # button = self.browser.find_element(By.NAME, "commit").click()
        # password.send_keys(Keys.ENTER)

##############################################################################################################


    def get_followers(self):
        self.browser.get("https://www.instagram.com/example/followers/")
        
        # Followers button click
        self.browser.find_element(By.XPATH, "//*[@id='mount_0_0_MX']/div/div/div/div[1]/div/div/div/div[1]/div[1]/section/main/div/ul/li[2]/a/div").click()
        
        time.sleep(3)

        # diaolog_box = self.browser.find_element(By.XPATH, "//div[@role='dialog']//div[1]//div[1]//div[1]//div[1]//div[2]//div[1]//div[1]//div[1]//div[2]//div[1]//div[1]//div[1]")
        diaolog_box = self.browser.find_element(By.XPATH, "//div[@class='._ab8w._ab94._ab99._ab9f._ab9k._ab9p._abcm']")
        followers = diaolog_box.find_elements(By.CSS_SELECTOR, "span")

        # follower_count = len(diaolog_box.find_elements(By.CSS_SELECTOR, "li"))
        # print = (f"Follower count of this page: {follower_count}")

    #     action = webdriver.ActionChains(self.browser)

    #     # Scrolling and updating follower count 
    #     while True:
    #         diaolog_box.click()
    #         action.key_down(Keys.SPACE).key_up(Keys.SPACE).perform()

    #         time.sleep(2)

    #         new_count = len(diaolog_box.find_elements(By.CSS_SELECTOR, "li"))

    #         if follower_count != new_count:
    #             follower_count = new_count
    #             print(f"Updated follower count is: {new_count}")
    #             time.sleep(2)
    #         else:
    #             break

        for user in followers:
            link = user.find_element(By.CSS_SELECTOR, "a").get_attribute("href")
            print(link)

##############################################################################################################

    # def auto_follow(self, username):
    #     self.browser.get("https://www.instagram.com/" + username)
    #     time.sleep(1)

    #     follow_button = self.browser.find_element(By.CLASS_NAME, c3)
    #     print(follow_button.text)
    #     if follow_button.text == "Follow" or "Takip Et":
    #         follow_button.click()

##############################################################################################################

    # def auto_unfollow(self, username):
    #     self.browser.get("https://www.instagram.com/" + username)
    #     time.sleep(1)

    #     follow_button = self.browser.find_element(By.CLASS_NAME, "")
    #     print(follow_button.text)
    #     if follow_button.text != "Following" or "Takip Ediliyor":
    #         follow_button.click()

##############################################################################################################

insta = Instagram(username, password)
insta.sign_in()
insta.get_followers()
# insta.auto_follow("btkakademi")

