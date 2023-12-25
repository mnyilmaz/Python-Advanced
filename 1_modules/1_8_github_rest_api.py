# BTK Academy
# Advanced Python Programming From Zero
# Lecture 1.8: Request Demo - Github Rest Api 
# python 1_8_github_rest_api.py
blank = "----------------------"

import requests, json

class Github:
    def __init__(self):
        self.api_url = "https://api.github.com"
        self.token = ''
    
    def get_user(self, username):
        response = requests.get(self.api_url + '/users/' + username)
        return response.json() # turns into 

    def get_repositories(self, username):
        response = requests.get(self.api_url + '/users/' + username + '/repos')
        return response.json() # turns into

    def generate_repositories(self, name):
        response = requests.get(self.api_url + '/user/repos?access_token=' + self.token, json={
            "name" : "Wonderland", 
            "description": "This is your first voyage", 
            "homepage" : "https://github.com", 
            "private" : False, 
            "has_issues" : True, 
            "has_projects" : True, 
            "has_wiki" : False
            })
        return response.json() # turns into
        
##############################################################################################################

github = Github()

while True:
    choice = input("1 - Find User\n2 - Get Repository\n3 - Generate Repository\nQ - Quit\nMake your choice: ")

    if choice == "Q":
        break
    else:
        if choice == "1":
            username = input("Please enter your username: ")
            result = github.get_user(username)
            print(f"Name: {result['name']}\nPublic Repositories: {result['public_repos']}\nFollower: {result['followers']}\n{blank}")

        elif choice == "2":
            username = input("Please enter your username: ")
            result = github.get_repositories(username)
            for repo in result:
                print(f"{repo['name']}\n{blank}")

        elif choice == "3":
            name = input("Please enter your repository name: ")
            result = github.generate_repositories(name)
            print(result)

        else:
            print(f"Incorrect Input!\n{blank}")
            
