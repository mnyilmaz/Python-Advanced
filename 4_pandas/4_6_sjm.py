# BTK Academy
# Advanced Python Programming From Zero
# Lecture 4.6: Pandas - Data Analysis - String Functions, Join and Merge
# python 4_6_sjm.py
blank = "----------------------"
import pandas as pd
import numpy as np

# String Functions

datas = pd.read_csv("imdb250.csv")
datas.dropna(inplace = True)

print(f"IMDB Data: \n{datas.head(1)}\n{blank}") 
print(f"IMDB Data Columns: \n{datas.columns}\n{blank}")

datas["Title"] = datas["Title"].str.upper()
print(f"IMDB Data Upper: \n{datas.head(1)}\n{blank}")
datas = pd.read_csv("imdb250.csv")

datas["Director"] = datas["Title"].str.find('r') # => returns index numbers of r
print(f"IMDB Data Index of 'r': \n{datas.head(1)}\n{blank}")
datas = pd.read_csv("imdb250.csv")

datas = datas['Director'].str.contains('Nolan')
print(f"IMDB Data 'Nolan': \n{datas.head(1)}\n{blank}") 
datas = pd.read_csv("imdb250.csv")

datas = datas['Title'].str.replace(' ', '-')
print(f"IMDB Data 'replace': \n{datas.head(1)}\n{blank}") 
datas = pd.read_csv("imdb250.csv")

datas[['First Name', 'Last Name']] = datas['Director'].loc[datas['Director'].str.split().str.len()==2].str.split(expand=True)
print(f"IMDB Data First and Last: \n{datas.head(1)}\n{blank}")

##############################################################################################################

# Join and Merge

drivers = {
            'Driver_ID'  : [16, 44, 63, 55, 4],
            'First_Name' : ["Charles", "Lewis", "George", "Carlos", "Lando"],
            'Last_Name'  : ["Leclerc", "Hamilton", "Russell", "Sainz", "Noris"],
            'Team_Name'  : ["Ferrari", "Mercedes", "Mercedes", "Ferrari", "McLaren"],
            'Points'     : [178, 146, 158, 156, 76]
}

teams = {
            'Team_Name'  : ["Ferrari", "Mercedes", "Mercedes", "Ferrari", "McLaren"],
            'Team_ID'    : [334, 304, 304, 334, 95],
            'Driver_ID'  : [16, 44, 11, 1, 4],
            'Team_Date'  : ["1997-10-16", "1985-01-07", "1998-02-05", "1994-09-01", "1999-11-13"],
}

df_drivers = pd.DataFrame(drivers, columns=["Driver_ID", "First_Name", "Last_Name", "Team_Name", "Points"])
df_teams = pd.DataFrame(teams, columns=["Team_Name", "Team_ID", "Driver_ID", "Team_Date"])

# print(f"Drivers: \n{df_drivers}\n{blank}")
# print(f"Teams: \n{df_teams}\n{blank}")

# concat_joint =pd.concat(df_drivers, df_teams) => concatenation

inner_joint = pd.merge(df_drivers, df_teams, how="inner")
# print(f"Inner Joint: \n{inner_joint}\n{blank}")

left_joint = pd.merge(df_drivers, df_teams, how="left") # prints all customers if there is no match prints NaN on right
# print(f"Left Joint: \n{left_joint}\n{blank}")

right_joint = pd.merge(df_drivers, df_teams, how="right") # prints all customers if there is no match prints NaN on left
# print(f"Left Joint: \n{right_joint}\n{blank}")

outer_joint = pd.merge(df_drivers, df_teams, how="outer")
# print(f"Left Joint: \n{outer_joint}\n{blank}")

##############################################################################################################

# DataFrame Methods

data = {
            'Column1' : [16, 44, 63, 55, 4],
            'Column2' : [334, 304, 304, 334, 95],
            'Column3' : ["Leclerc", "Hamilton", "Russell", "Sainz", "Noris"],
}

def sqrt(x):
    return x*x

sqrt_2 = lambda x: x*x

df = pd.DataFrame(data)
print(f"Data: \n{df}\n{blank}")

uniq = df["Column2"].unique()
print(f"Uniqe: {uniq}\n{blank}") # get uniqe elements

n_uniq = uniq = df["Column2"].nunique()
print(f"Number of Uniqes: {n_uniq}\n{blank}") # get number of uniqe elements

cnt = df["Column2"].value_counts()
print(f"Count: \n{cnt}\n{blank}") # Counts repeated ones

srt = df["Column1"].sort_values(ascending=False) # it will decrease
# srt = df.sort_values("Column1")
print(f"Sorting: \n{srt}\n{blank}") # sorting hat

fnctn = df["Column2"].apply(sqrt)
# fnctn = df["Column2"].apply(sqrt_2) => same as
# fnctn = df["Column2"].apply(lambda x: x*x) => same as
fnctn_len = df["Column3"].apply(len)
print(f"Applying a function: \n{fnctn}\n{blank}") # applies function
print(f"Applying a function #2: \n{fnctn_len}\n{blank}") # applies function

pvt = df.pivot_table(index="Column1", columns="Column3", values="Column2")
print(f"Pivoting: \n{pvt}\n{blank}") # pivot table


# result = df.info
# result = df.columns
# result = len(df.columns)
# result = df.index
# result = len(df.index)

