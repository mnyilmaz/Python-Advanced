# BTK Academy
# Advanced Python Programming From Zero
# Lecture 1.13: Beautifulsoup - Amazon 
# python 1_13_beautifulsoup_amazon.py
blank = "----------------------"

import requests
from bs4 import BeautifulSoup

url = "https://www.amazon.com.tr/s?i=sports&rh=n%3A27910119031&fs=true&qid=1659910070&ref=sr_pg_1"

# response = requests.get(url)
# print(response) # <Response [200]> successful

# content = response.content
# print(content) 

html = requests.get(url).content
soup = BeautifulSoup(html, "html.parser")

list = soup.find("img", {"alt" : "Stanley Klasik Trigger Action Termos Bardak 0,59 Lt, Yeşil"}).find_all() 
# find tbody then specify class area after all find tr and limit only with 1
print(list)
print(blank)

# for tr in list:
#     title = tr.find("td", {"class" : "titleColumn"}).find("a").text
#     year = tr.find("td", {"class" : "titleColumn"}).find("span").text.strip("()")
#     rating = tr.find("td", {"class" : "ratingColumn imdbRating"}).find("strong").text
#     print(f"Movie: {title}\nYear: {year}\nRating: {rating}\n{blank}")


