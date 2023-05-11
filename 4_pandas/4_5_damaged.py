# BTK Academy
# Advanced Python Programming From Zero
# Lecture 4.5: Pandas - Data Analysis - Damaged and Lost
# python 4_5_damaged.py
blank = "----------------------"
import pandas as pd
import numpy as np

data = np.random.randint(10,100,15).reshape(5,3)
df = pd.DataFrame(data, index=["A", "C", "E", "F", "H"], columns=["Column1","Column2", "Column3"])
df = df.reindex(["A", "B", "C", "D","E", "F", "G","H"])
print(f"Damaged Original: \n{df}\n{blank}") # b,d,g row is NaN

new_col = [np.nan, 30, np.nan, 51, np.nan, 30, np.nan, 10]
df["Column4"] = new_col
print(f"Damaged Added: \n{df}\n{blank}") # b,d,g row is NaN

remove_col = df.drop("Column1", axis=1)
# remove_col = df.drop(["Column1", "Column2"], axis=1)
remove_row = df.drop("A", axis=0)
# remove_row = df.drop(["A", "C"], axis=0)
print(f"Column Removed: \n{remove_col}\n{blank}") # Column1 removed
print(f"Row Removed: \n{remove_row}\n{blank}") # A removed

# Identifying NaN
idntfy = df.isnull() # NaN will appear as True
# idntfy = df.notnull() # NaN will appear as False
print(f"Identification of NaN: \n{idntfy}\n{blank}") 

# idntfy = df.isnull().sum() # Counts NaN's
# idntfy = df["Column1"].isnull() # Get nulls at Column1
# idntfy = df[["Column1"].isnull()] # Get nulls at Column1
idntfy = df.dropna()["Column1"] # original axis value is axis = 0 (which means row)
# idntfy = df.dropna(how = "any") # removes any NaN from dataframe
# idntfy = df.dropna(how = "all") # only removes row/rows full of NaN
# idntfy = df.dropna(subset=["Column1", "Column2"], how="all") # search NaN's only in column 1 and column 2
# idntfy = df.dropna(thresh = 2) # if there are at least 2 non NaN value, doesn't remove
print(f"Down of the NaN: \n{idntfy}\n{blank}") 

# Filling NaN value spaces
fill = df.fillna(value ="no input")
print(f"Rise of the NaN: \n{fill}\n{blank}") 










