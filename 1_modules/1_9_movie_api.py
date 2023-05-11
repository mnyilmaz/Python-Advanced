# BTK Academy
# Advanced Python Programming From Zero
# Lecture 1.9: Request Demo - Movie Api 
# python 1_9_movie_api.py
blank = "----------------------"

# https://www.themoviedb.org => archive for movies and tv-series
# Use themoviedb's api in you application
# Search according to keyword
# Most popular movie list
# Upcoming movie list

import requests, json

class the_movie_DB:
    def __init__(self):
        self.api_url = "url"
        self.api_key = "key"

    def get_populars(self):
        response = requests.get(f"{self.api_url}/movie/popular?api_key={self.api_key}&language=en-US&page=1")
        return response.json()

    def get_search_results(self, keyword):
        response = requests.get(f"{self.api_url}/search/keyword?api_key={self.api_key}&query={keyword}&page=1")
        return response.json()

##############################################################################################################

movie = the_movie_DB()

while True:
    choice = input("1 - Popular Movies\n2 - Search Movies\nQ - Quit\nMake your choice: ")

    if choice == "Q":
        break
    else:
        if choice == "1":
            movies = movie.get_populars()
            for movie in movies['results']:
                print(movie['title'])

        elif choice == "2":
            keyword = input("Please enter your keyword: ")
            movies = movie.get_search_results(keyword)
            for movie in movies['results']:
                print(movie['name'])
        else:
            print(f"Incorrect Input!\n{blank}")