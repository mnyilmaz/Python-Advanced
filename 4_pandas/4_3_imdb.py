# BTK Academy
# Advanced Python Programming From Zero
# Lecture 4.3: Pandas - Data Analysis Working With DataFrame and IMDB Application
# python 4_3_imdb.py
blank = "----------------------"
import pandas as pd
import numpy as np

# Get IMDB Data using DataFrame and Pandas

# Milestone 1: Get info about file
file = pd.read_csv("imdb250.csv")
info = file.info
print(f"M1 - Info:\n {info}\n{blank}") 

##############################################################################################################

# Milestone 2: Get first five record
first_five = file.head(5)
print(f"M2 - First five record:\n {first_five}\n{blank}") 

##############################################################################################################

# Milestone 3: Get first ten record
first_ten = file.head(10)
print(f"M3 - First ten record:\n {first_ten}\n{blank}") 

##############################################################################################################

# Milestone 4: Get last five record
last_five = file.tail(5)
print(f"M4 - Last five record:\n {last_five}\n{blank}") 

##############################################################################################################

# Milestone 5: Get last ten record
last_ten = file.tail(10)
print(f"M5 - Last ten record:\n {last_ten}\n{blank}") 

##############################################################################################################

# Milestone 6: Get only the "Title" column
title = file["Title"]
print(f"M6 - Only 'Title' Column:\n {title}\n{blank}") 

##############################################################################################################

# Milestone 7: Get only the first five rows of "Title" column
title_five = file["Title"].head(5)
print(f"M7 - Only first five of the 'Title' Column:\n {title_five}\n{blank}") 

##############################################################################################################

# Milestone 8: Get only the first five rows of "Title" and "Rating" column
title_rating_five = file[["Title", "Rating"]].head(5)
print(f"M8 - Only first five of the 'Title' and 'Rating 'Column:\n {title_rating_five}\n{blank}") 

##############################################################################################################

# Milestone 9: Get only the last seven rows of "Title" and "Rating" column
title_rating_seven = file[["Title", "Rating"]].tail(7)
print(f"M9 - Only last seven of the 'Title' and 'Rating 'Column:\n {title_rating_seven}\n{blank}") 

##############################################################################################################

# Milestone 10: Get only the second five rows of "Title" and "Rating" column
title_rating_second = file[5:10][["Title", "Rating"]].head(5)
print(f"M10 - Only second five of the 'Title' and 'Rating 'Column:\n {title_rating_second}\n{blank}") 

##############################################################################################################

# Milestone 11: Get only the first 50 records of "Title" and "Rating" column if movie rating is >= 8.0
rating = file[file["Rating"] > 8][["Title", "Rating"]].head(50)
print(f"M11 - Only the first 50 records of 'Title' and 'Rating 'Column if rating is >= 8.0:\n {rating}\n{blank}") 

##############################################################################################################

# Milestone 12: Get movies that their release date is between 2014-2015
date = file[(file["Date"] <= 2015) &  (file["Date"] >= 2014)]
print(f"M12 - Only the movies that their release date is between 2014-2015:\n {date}\n{blank}") 

##############################################################################################################

# Milestone 13: Get movies that their review numbers is over 100.000 or rating point is between 8-9
review = file[(file["Votes"] >= 100000) | ((file["Rating"] >= 8) & (file["Rating"] <= 9))][["Title", "Rating", "Votes"]]
print(f"M13 - Review number is over 100.000 or rating point is between 8-9:\n {review}\n{blank}") 




