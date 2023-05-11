# BTK Academy
# Advanced Python Programming From Zero
# Lecture 2.3: Page Interaction with Selenium
# python 2_3_page_interaction.py
blank = "----------------------"

# Page Interaction  
from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Edge()
url = "https://www.github.com"
driver.get(url)

driver.maximize_window()
# search_input = driver.find_element(By.NAME, "q")
search_input = driver.find_element(By.XPATH, "/html/body/div[1]/header/div/div[2]/div[2]/div[1]/div/div/form/label/input[1]")

time.sleep(2)

search_input.send_keys("python")
time.sleep(2)

search_input.send_keys(Keys.ENTER)
time.sleep(2)

# result = driver.find_elements(By.CSS_SELECTOR, ".repo-list-item h3 a")
# for element in result:
#      print(element.text)

result = driver.page_source
print(result)

driver.close()