# BTK Academy
# Advanced Python Programming From Zero
# Lecture 4.7: Pandas - Data Analysis Working With DataFrame and NBA Application
# python 4_7_nba.py
blank = "----------------------"
from cmath import nan
import pandas as pd
import numpy as np

# Get NBA Data using DataFrame and Pandas

# Milestone 1: Get first ten record
file = pd.read_csv("all_seasons.csv")
first_ten = file.head(10)
print(f"M1 - First ten record:\n{first_ten}\n{blank}") 

##############################################################################################################

# Milestone 2: Get total records
total = len(file)
print(f"M2 - Total record: {total}\n{blank}") 

##############################################################################################################

# Milestone 3: Get age mean of all players' age
data_frame = pd.DataFrame(file)
mean_all = data_frame['age'].mean()

print(f"M3 - Mean of all players' age: {mean_all}\n{blank}") 

##############################################################################################################

# Milestone 4: Get max age
max_age = data_frame['age'].max()
print(f"M4 - Max age is: {max_age}\n{blank}") 

##############################################################################################################

# Milestone 5: Get the eldest player
eldest = file[(file["age"] == max_age)]["player_name"]
print(f"M5 - The eldest player is:\n{eldest}\n{blank}") 

##############################################################################################################

# Milestone 6: Get players' team who at the age of 20-25
twenty_five = file[(file["age"] >= 20) & (file["age"] <= 25)].sort_values("age", ascending=False)
print(f"M6 - players' team who at the age of 20-25:\n{twenty_five}\n{blank}") 

##############################################################################################################

# Milestone 7: Who is John Holland?
# john_holland = file["player_name"].str.contains("John Holland")
john_holland = file[(file["player_name"] == "John Holland")]
print(f"M7 - John Holland:\n{john_holland}\n{blank}")

##############################################################################################################

# Milestone 8: Get average age info according to teams
team = data_frame.groupby("team").agg(np.mean)
print(f"M8 - Team Grouping:\n{team}\n{blank}") 

##############################################################################################################

# Milestone 9: How many teams are in this file?
team_len = len(data_frame.groupby("team"))
# team_len = data_frame["team"].unique()
print(f"M9 - There are {team_len} teams in this list.\n{blank}") 

##############################################################################################################

# Milestone 10: How many players does play in these teams?
player_amount =  data_frame["team"].value_counts()
print(f"M10 - Player amount per team:\n{player_amount}\n{blank}") 

##############################################################################################################

# Milestone 11: Find records including 'and'
inc_and = file[file["player_name"].str.contains("and")]
# inc_and = file[file["player_name"] == "and"]
print(f"M11 - Records that including 'and':\n{inc_and}\n{blank}") 
