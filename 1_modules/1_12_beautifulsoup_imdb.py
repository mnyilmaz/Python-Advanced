# BTK Academy
# Advanced Python Programming From Zero
# Lecture 1.12: Beautifulsoup - IMDB 
# python 1_12_beautifulsoup_imdb.py
blank = "----------------------"

import requests
from bs4 import BeautifulSoup

url = "https://www.imdb.com/chart/top?ref_=nv_mv_250"

# response = requests.get(url)
# print(response) # <Response [200]> successful

# content = response.content
# print(content) 

html = requests.get(url).content
soup = BeautifulSoup(html, "html.parser")

list = soup.find("tbody", {"class" : "lister-list"}).find_all("tr", limit=250) 
# find tbody then specify class area after all find tr and limit only with 1
# print(list)
print(blank)

for tr in list:
    title = tr.find("td", {"class" : "titleColumn"}).find("a").text
    year = tr.find("td", {"class" : "titleColumn"}).find("span").text.strip("()")
    rating = tr.find("td", {"class" : "ratingColumn imdbRating"}).find("strong").text
    print(f"Movie: {title}\nYear: {year}\nRating: {rating}\n{blank}")


