# BTK Academy
# Advanced Python Programming From Zero
# Lecture 2.4: Get Github Followers with Using Selenium
# python 2_4_github.py
blank = "----------------------"

# Get Github Followers
from github_user_info import username, password
from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


class Github:
    def __init__(self, username, password):
        self.browser = webdriver.Edge()
        self.username = username
        self.password = password
        self.followers = []

##############################################################################################################

    def sign_in(self):
        self.browser.get("https://github.com/login")
        time.sleep(1)
        username = self.browser.find_element(By.XPATH, "//*[@id='login_field']").send_keys(self.username)
        password = self.browser.find_element(By.XPATH, "//*[@id='password']").send_keys(self.password)
        time.sleep(1)
        button = self.browser.find_element(By.NAME, "commit").click()
        # button = self.browser.find_element(By.XPATH, "//*[@id='login']/div[4]/form/div/input[12]").click()

##############################################################################################################

    def get_name(self):

        items = self.browser.find_elements(By.CSS_SELECTOR, ".d-table.table-fixed") # inside d-table class div
        for i in items:
            self.followers.append(i.find_element(By.CSS_SELECTOR, ".f4.Link--primary").text) # span class names Link...
   
##############################################################################################################

    def get_followers(self):
        self.browser.get("https://github.com/Calalari?tab=followers")
        # self.browser.get("https://github.com/{self.username}?tab=followers")
        time.sleep(2)
        self.get_name()
        
        # If you have more than 1 followers page
        # while True:
        #     links = self.browser.find_element(By.CLASS_NAME, "BtnGroup").find_elements(By.TAG_NAME, "a")

        #     if len(links) == 1:
        #         if links[0].text == "Next":
        #             links[0].click()
        #             time.sleep(2)

        #             self.get_name()  
        #         else: 
        #             break

        #     else:
        #         for link in links:
        #             if link.text == "Next":
        #                 link.click()
        #                 time.sleep(2)
        #                 self.get_name()
        #             else: 
        #                 continue

##############################################################################################################

github = Github(username, password)
github.sign_in()
time.sleep(2)

github.get_followers()
print(github.followers)
print(len(github.followers))
github.browser.close()

   


