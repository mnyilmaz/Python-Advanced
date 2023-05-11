# BTK Academy
# Advanced Python Programming From Zero
# Lecture 1.6: Request Module in Python 
# python 1_6_request.py
blank = "----------------------"

import json
print(json.__file__) # locate json file
print(blank)

# Requests Module
# The requests module allows you to send HTTP requests using Python. 

import requests

result = requests.get("https://jsonplaceholder.typicode.com/todos")
print(result) # response 200 - so successfull
print(blank)

# Getting json record
js = result.text
print(js)
print(blank)

# Turn json into dict
new = json.loads(js)
print(new[0]["title"])
print(blank)

for i in new:
    print(i["title"])
