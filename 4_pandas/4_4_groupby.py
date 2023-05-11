# BTK Academy
# Advanced Python Programming From Zero
# Lecture 4.4: Pandas - Data Analysis Working With Groupby
# python 4_4_groupby.py
blank = "----------------------"

# Groupby
# groupby() function is used to split the data into groups based on some criteria. 
# pandas objects can be split on any of their axes. 
# The abstract definition of grouping is to provide a mapping of labels to group names.

import pandas as pd
import numpy as np 

drivers = {
            'Driver'   : ["Charles Leclerc", "Lewis Hamilton", "George Russell", "Carlos Sainz", "Lando Noris"],
            'Team'     : ["Ferrari", "Mercedes", "Mercedes", "Ferrari", "McLaren"],
            'Age'      : [24, 37, 24, 27, 22],
            'Homeland' : ["Monaco", "England", "England", "Spain", "England"],
            'Points'   : [178, 146, 158, 156, 76]
}

data_frame = pd.DataFrame(drivers)
result = data_frame
print(f"Drivers: \n{result}\n{blank}") 

# Grouping
sum = data_frame["Points"].sum()
print(f"Sum of All Drivers' Points: {sum}\n{blank}") 

group = data_frame.groupby("Team").groups
group = data_frame.groupby(["Team", "Homeland"]).groups

homeland = data_frame.groupby("Homeland")
for name, group in homeland:
    print(f"Homeland: \n{name}\n{blank}")
    print(f"Group: \n{group}\n{blank}") 

ferrari = data_frame.groupby("Team").get_group("Ferrari")
print(f"Ferrari Drivers: \n{ferrari}\n{blank}") 

team = data_frame.groupby("Team").sum()
team_mean = data_frame.groupby("Team").mean()
team_age_mean = data_frame.groupby("Team")["Age"].mean()
homeland_age_mean = data_frame.groupby("Homeland")["Age"].mean()
homeland_driver_count = data_frame.groupby("Homeland")["Driver"].count()
# max = data_frame.groupby("Team")["Age"].max()
# min = data_frame.groupby("Team")["Points"].min()
# max = data_frame.groupby("Team")["Age"].max()["Ferrari"] => reveals the eldest driver in Ferrari
ag = data_frame.groupby("Team").agg(np.mean)
# ag_2 = data_frame.groupby("Team")["Points"].agg(np.sum, np.mean, np.max, np.min).loc["Ferrari"]

print(f"Team Grouping Sum: \n{team}\n{blank}") 
print(f"Team Grouping Mean: \n{team_mean}\n{blank}")
print(f"Team Age Mean: \n{team_age_mean}\n{blank}") 
print(f"Homeland Age Mean: \n{homeland_age_mean}\n{blank}")
print(f"Homeland Driver Count: \n{homeland_driver_count}\n{blank}") 
print(f"Average per Team: \n{ag}\n{blank}") 









