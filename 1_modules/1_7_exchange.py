# BTK Academy
# Advanced Python Programming From Zero
# Lecture 1.7: Request Demo - An Exchange Application 
# python 1_7_exchange.py
blank = "----------------------"
import requests, json

# https://api.exchangerate.host/latest

# Exchange Application

# Getting data from api
api_url = "https://api.exchangerate.host/latest"

# Inputs from customer
inp = input("Currency type: ")
out = input("Type of currency received: ")
amount = int(input(f"How much {inp} do you want to exchange?: "))


# Turn json into dict
result = requests.get(api_url+inp)
result = json.loads(result.text)

print("1 {0} = {1} {2}".format(inp, result["rates"][out], out))
print("{0} {1} = {2} {3}".format(amount, inp, amount*result["rates"][out], out))


