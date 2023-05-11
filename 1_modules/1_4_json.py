# BTK Academy
# Advanced Python Programming From Zero
# Lecture 1.4: Json Module in Python 
# python 1_4_json.py
blank = "----------------------"

# Json Module
# JavaScript Object Notation (JSON) is a standardized format commonly used to transfer data as text that can 
# be sent over a network. It's used by lots of APIs and Databases, and it's easy for both humans and machines 
# to read. JSON represents objects as name/value pairs, just like a Python dictionary.

# Dictionary Repetition
person = {"name":"Alice",
          "languages": ["English, German"]}

name = person["name"]
print(name)
print(blank)

languages = person["languages"]
print(languages)
print(blank)

##############################################################################################################

import json

mad = '{"name":"Hatter", "languages":["English,German"]}'

# JSON string to Dict
js = json.loads(mad)
print(f"New formatted json is:{js}\nType of json is now {type(js)}")
print(blank)


# Read JSON from a file
with open("wonderland.json") as file:
    data = json.load(file)
    print(f"New formatted json is:{data}\nType of json is now {type(data)}")
print(blank)

# Dict to JSON
underland ={
    "name" : "Absolem",
    "languages" : "English"
}

dj = json.dumps(underland)
print(f"New formatted dictionary is:{dj}\nType of dictionary is now {type(dj)}")

with open("wonderland.json", "a") as f:
    json.dump(underland, f)
print(blank)

new = '{"name":"The Rabbit", "languages":["English,German"]}'
now = json.loads(new)
correct = json.dumps(new, indent=4, sort_keys=True)
print(correct)


