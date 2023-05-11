# BTK Academy
# Advanced Python Programming From Zero
# Lecture 2.1: Selenium
# python 2_1_selenium.py
blank = "----------------------"

# Selenium
# Selenium is an open-source web-based automation tool/lib. 
# Python language is used with Selenium for testing.
# Automatic login

from selenium import webdriver 
import time

# Running a page through webdriver (using microsoft edge)
driver = webdriver.Edge()
url = "https://www.github.com"
driver.get(url) # that will automatically open url

time.sleep(2) # wait 2 scnd after opening the page
driver.maximize_window() # maximize window
driver.save_screenshot("github_hp.png")

url = "http://github.com/calalari"
driver.get(url)

print(driver.title) # print title of the page on console
if "Calalari" in driver.title:
    driver.save_screenshot("calalari.png")

time.sleep(2) # wait 2 scnd

# driver.minimize_window() # minimize window
# time.sleep(2) # wait 2 scnd

driver.back() # loads previous website
time.sleep(2) # wait 2 scnd

driver.close() # close the page

##############################################################################################################


