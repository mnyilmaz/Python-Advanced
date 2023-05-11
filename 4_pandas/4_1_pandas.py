# BTK Academy
# Advanced Python Programming From Zero
# Lecture 4.1: Pandas - Data Analysis
# python 4_1_pandas.py
blank = "----------------------"

# Pandas
# pandas is a Python package providing fast, flexible, and expressive data structures designed to make 
# working with “relational” or “labeled” data both easy and intuitive. 
# It aims to be the fundamental high-level building block for doing practical, real-world data analysis in Python.

import sqlite3
import pandas as pd
import numpy as np


# enterence to pandas
# df = pd.read_csv("data/sample.csv")
# df = pd.read_json("data/sample.json", encoding="UTF-8")
# df = pd.read_excel("data/sample.xlsx")

# connection = sqlite3.connect("data/sample.db")
# db = pd.read_sql_query("SELECT * from STUDENTS", connection)
# print(f"{df}\n{blank}")

##############################################################################################################

# Usage of pandas

# Data
numbers = [20,30,40,50]
letters = ["a","b","c","d"]
scalar = 7
dict = {"a": 10, "b":20, "c":30, "d":40}
random = np.random.randint(0,100,7)

# pandas_series = pd.Series() -> print(f"{pandas_series}\n{blank}") # Series([], dtype: float64) 
pandas_numbers = pd.Series(numbers)
pandas_letters = pd.Series(letters)
pandas_scalar = pd.Series(scalar, [1,3,4,5]) # [] determines index number
pandas_dict = pd.Series(dict)
pandas_random = pd.Series(random)

print(f"Numbers: \n{pandas_numbers}\n{blank}") 
print(f"Letters: \n{pandas_letters}\n{blank}") 
print(f"Scalar: \n{pandas_scalar}\n{blank}") 
print(f"Dict: \n{pandas_dict}\n{blank}") 
print(f"Random: \n{pandas_random}\n{blank}") 

# result = pandas_numbers[0] -> get first value
# result = pandas_numbers[-1] -> get last value
# result = pandas_numbers[:2] -> get until second value
# result = pandas_numbers[-2:] -> get last value
# result = pandas_numbers.ndim -> get dimension value
# result = pandas_numbers.dtype -> get type
# result = pandas_numbers.shape -> get shape
# result = pandas_numbers.sum() -> get sum
# result = pandas_numbers.max() -> get max
# result = pandas_numbers.min() -> get min
# result = pandas_numbers.sqrt() -> get square
# result = pandas_numbers + pandas_numbers -> sum of these two
# result = pandas_numbers + 50 -> sum of these two
# result = pandas_numbers > 50 -> logical operations (returns boolean)
# result = pandas_numbers % 2 == 0 -> logical operations (returns boolean)

# Practice: Pandas

volvo_21 = pd.Series([20, 30, 40, 10], ["xc40", "xc60", "xc90", "s60"])
volvo_22 = pd.Series([40, 30, 20, 10], ["xc40", "xc60", "xc90", "s90"])
total = volvo_21 + volvo_22
print(f"Total: \n{total}\n{blank}")
total = total["xc40"]
print(f"XC40: {total}\n{blank}") 

##############################################################################################################

# Working with DataFrames (df)
# DataFrame is a 2-dimensional labeled data structure with columns of potentially different types. 
# You can think of it like a spreadsheet or SQL table, or a dict of Series objects.

# # # # # # # # # #         # # # # # # # # # #         # # # # #  DATA FRAMES  # # # # # 
#      apples     #         #      oranges    #         #       apples     oranges      #
#   0     3       #         #   0     0       #         #   0      3          0         #
#   -----------   #         #   -----------   #         #   ------------ ------------   #
#   1     2       #         #   1     3       #         #   1      2          3         #
#   -----------   #         #   -----------   #         #   ------------ ------------   #
#   2     0       #         #   2     7       #         #   2      0          7         #
#   -----------   #         #   -----------   #         #   ------------ ------------   #
#   3     1       #         #   3     2       #         #   3      1          2         #
# # # # # # # # # #         # # # # # # # # # #         # # # # # # # # # # # # # # # # # 

# First DataFrame
s_1 = pd.Series([3,2,0,1])
s_2 = pd.Series([0,3,7,2])

data = {"apples": s_1, "oranges" : s_2} # data = dict(apples = s_1, oranges = s_2) -> that didn't work for me
 
# df = pd.DataFrame(data)
# print(f"DataFrame:\n {df}\n{blank}") 

# df = pd.DataFrame()
# df = pd.DataFrame([1,2,3,4])

list = (["Alice",70], ["Hatter",45], ["Chess",87])
df = pd.DataFrame(list, columns=["Names", "Grades"], index=[1,2,3])
# df = pd.DataFrame(data_2, [1,2,3,4], ["Names", "Grades"]) if you don't mention parameter names it has it's own que

dict_list = [{"Names": "Alice", "Grades" : 70}, {"Names": "Hatter", "Grades" : 45}, {"Names": "Chess", "Grades" : 87}]
df_1 = pd.DataFrame(dict_list, index=[1,2,3])

print(f"DataFrame:\n {df}\n{blank}")
print(f"DataFrame:\n {df_1}\n{blank}") 


















