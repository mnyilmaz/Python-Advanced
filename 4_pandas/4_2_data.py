# BTK Academy
# Advanced Python Programming From Zero
# Lecture 4.2: Pandas - Data Analysis Working With DataFrame
# python 4_2_data.py
blank = "----------------------"

# Reading Data from Different File Type

import pandas as pd
from numpy.random import randn
import numpy as np

# Reading CSV
nba = pd.read_csv("all_seasons.csv")
print(f"DataFrame:\n {nba}\n{blank}") 

# Reading JSON
formula = pd.read_json("formula.json")
print(f"DataFrame:\n {formula}\n{blank}") 


# Reading XLSX
book = pd.read_excel("book.xlsx")
print(f"DataFrame:\n {book}\n{blank}") 

# Reading SQLDB
# connection = sqlite3.connect("sample.db")
# sqdb = pd.read_sql_query("SELECT * FROM students", connection)
# print(f"DataFrame:\n {sqdb}\n{blank}") 

##############################################################################################################

# Selections in DataFrames

df = pd.DataFrame(randn(3,3), index=["A","B","C"], columns=["Column 1","Column 2","Column 3"])
col = df["Column 1"]
typ = type(col)
loc = df.loc["A"]
# loc = loc["row", "column"] => loc["row"] => loc[":", "column"]
col_1 = df.loc[:, "Column 1"] # Column 1
# col_1 = df.loc[:, "Column 1" : "Column 3"] # Between col 1 and col 3
row_1 = df.loc["A", :] # Row 1
# index = df.iloc[2] # => use this if your index is different
a_2 = df.loc["A", "Column 2"]
a_b_2 = df.loc[["A","B"], ["Column 1","Column 2"]]
df["Column 4"] = pd.Series(randn(3), index=["A","B","C"]) # adding a new column
df["Column 5"] = df["Column 1"] + df["Column 3"] # adding a new column
removed = df.drop("Column 5", axis=1, inplace=False) # before printing it has already been deleted from matrix if TRUE

print(f"DataFrame:\n {df}\n{blank}") 
print(f"Column 1:\n {col}\n{blank}") 
print(f"Type:\n {typ}\n{blank}")  #  <class 'pandas.core.series.Series'>
print(f"A:\n {loc}\n{blank}") 
print(f"Column 1:\n {col_1}\n{blank}") 
print(f"Row 1:\n {row_1}\n{blank}") 
print(f"A x Column 2:\n {a_2}\n{blank}") 
print(f"A_B x Column 1 - Column 2:\n {a_b_2}\n{blank}")
print(f"Adding Column 4:\n {df}\n{blank}") 
print(f"Removing Column 5:\n {removed}\n{blank}") 

##############################################################################################################

# Filtering Data's inside DataFrame's

data = np.random.randint(10,100,75).reshape(15,5)
dff = pd.DataFrame(data, columns=["Column 1","Column 2","Column 3","Column 4","Column 5"])

rslt =  dff
columns =  dff.columns
rows_h = dff.head(5) # get first 5 rows
# rows = dff.head(10) # get first 10 rows
rows_t = dff.tail(5) # get last 5 rows
column_1 = dff["Column 1"].head(5)
# column_1 = dff[["Column 1", "Column 2"]].head(5) => get first five of first two cloumns
# column_1 = dff[5:15][["Column 1", "Column 2"]].head(5)

criteria = dff > 33 # returns True-False
criteria = dff[dff > 33] # returns True values as original value, returns False values as NaN
# criteria = dff[dff["Column 1"] > 33][["Column 1"]] # returns only for column 1 
# criteria = dff[(dff["Column 1"] > 50) & (dff["Column 1"] <= 70)][["Column 1"]] # returns only for column 1 (and)
# criteria = dff[(dff["Column 1"] > 50) | (dff["Column 1"] <= 70)][["Column 1"]] # returns only for column 1 (or)

print(f"Data:\n {data}\n{blank}") 
print(f"DataFrame:\n {dff}\n{blank}")
print(f"Columns:\n {columns}\n{blank}")
print(f"First five rows:\n {rows_h}\n{blank}") 
print(f"Last five rows:\n {rows_t}\n{blank}") 
print(f"First five rows only column 1:\n {column_1}\n{blank}") 
print(f"Criteria greater than 33:\n {criteria}\n{blank}") 
