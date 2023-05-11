# BTK Academy
# Advanced Python Programming From Zero
# Lecture 5.1: Matplotlib - Data Visualisation
# python 5_1_matplotlib.py
blank = "----------------------"

# Matplotlib is a cross-platform, data visualization and graphical plotting library for Python and its numerical extension NumPy.
# Use documentation for more specific graphs

import matplotlib.pyplot as plt
import numpy as np

""" Example 1 """
# x = [1,2,3,4]
# y = [1,4,9,16]

# plt.plot(x,y, "o--r") 
# plt.axis([0,6,0,20]) # x and y coordinate range [min, max]
# plt.plot(x,y, "--g", color="red", linewidth= "2") # dotted line # marker, line, color order => [m][l][c]

# plt.title("Example Graph")
# plt.xlabel("X Label")
# plt.ylabel("Y Label")
# plt.show()

""" Example 2 """
# x = np.linspace(0,2,100)

# For getting two seperate graphs
# fig, axs = plt.subplots(2)
# axs[0].plot(x, x, color = "blue")
# axs[0].set_title("Linear")
# axs[1].plot(x, x**2, color = "red")
# axs[1].set_title("Quadratic")
# plt.tight_layout()

# plt.plot(x, x, label = "Linear", color = "blue")
# plt.plot(x, x**2, label = "Quadratic", color = "red")
# plt.plot(x, x**3, label = "Cubic", color = "green")

# plt.title("Example Graph")
# plt.xlabel("X Label")
# plt.ylabel("Y Label")
# plt.legend() # reveals names according to colors
# plt.show()

""" Example 3 - Stack Plot """
# year = [2009, 2010, 2011, 2012, 2013, 2014, 2015]

# lewis = [0, 0, 0, 0, 0, 1, 1]
# seb = [0, 1, 1, 1, 1, 0, 0]
# jenson = [1, 0, 0, 0, 0, 0, 0]

# plt.plot([], [], color = "g", label = "Lewis Hamilton")
# plt.plot([], [], color = "b", label = "Sebastian Vettel")
# plt.plot([], [], color = "gray", label = "Jenson Button" )

# plt.stackplot(year, lewis, seb, jenson, colors =["g", "b", "gray"])

# plt.title("Championships According to Years")
# plt.xlabel("Year")
# plt.ylabel("Championship")
# plt.legend() # reveals names according to colors
# plt.show()

""" Example 4 - Pie Chart """
# championship_types = "Podiums", "DHL Fastest Lap", "GPs Entered" 

# championships = [18,7,95]
# colors = ["red", "purple", "yellow"]

# plt.pie(championships, labels = championship_types, colors = colors, shadow= True, explode=(0.05, 0.05, 0.05), autopct= "%1.1f%%")
# plt.title("Charles Leclerc's Standing Since Debut")
# plt.show()

""" Example 5 - Bar Graph """
# plt.bar([0.25, 1.25, 2.25, 3.25, 4.25], [50, 40, 70, 80, 20], label = "Ferrari", width=.5, color = "red")
# plt.bar([0.75, 1.75, 2.75, 3.75, 4.75], [80, 20, 20, 50, 60], label = "Mercedes", width=.5, color = "green")

# plt.title("Ferrari vs. Mercedes on Formula 1 Championship")
# plt.legend() # reveals names according to colors
# plt.show()

""" Example 6 - Histogram Graph """
# ages = [22, 55, 62, 45, 57, 12, 34, 56, 23, 21, 16, 34, 89, 32, 111, 39, 37, 87, 45, 29, 4, 2, 7]
# age_groups = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

# plt.hist(ages, age_groups, histtype="bar", rwidth=0.8)
# plt.xlabel("Age Groups")
# plt.ylabel("Amount of People")

# plt.title("Histogram Graph")
# plt.legend() # reveals names according to colors
# plt.show()

""" Example 7 - Importing Data """
import pandas as pd

df = pd.read_csv("imdb250.csv")

df = df.drop(["Rating"], axis = 1).groupby("Votes").mean()

df.plot(subplots=True)
plt.legend()
plt.show()
