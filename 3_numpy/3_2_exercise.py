# BTK Academy
# Advanced Python Programming From Zero
# Lecture 3.2: NumPy - Data Analysis Exercise
# python 3_2_exercise.py
blank = "----------------------"
import numpy as np

# Exercise - Working with numPy

# Question 1 - Generate a numPy array that includes (10, 15, 30, 45, 60)
q_1 = np.array([10, 15, 30, 45, 60])
print(f"Q1: {q_1}\n{blank}")

##############################################################################################################

# Question 2 - Generate a numPy array between 5-15
q_2 = np.arange(5,15)
print(f"Q2: {q_2}\n{blank}")

##############################################################################################################

# Question 3 - Generate a numPy array between 5-100 and let it increase by 5
q_3 = np.arange(5,100,5)
print(f"Q3: {q_3}\n{blank}")

##############################################################################################################

# Question 4 - Generate 10 element numPy array that made up of zeros
q_4 = np.zeros(10)
print(f"Q4: {q_4}\n{blank}")

##############################################################################################################

# Question 5 - Generate 10 element numPy array that made up of ones
q_5 = np.ones(10)
print(f"Q5: {q_5}\n{blank}")

##############################################################################################################

# Question 6 - Generate five elemented equally divided numPy array between 0-100 
q_6 = np.linspace(0,100,5)
print(f"Q6: {q_6}\n{blank}")

##############################################################################################################

# Question 7 - Generate 5 elemented integer numPy array between 10-30
q_7 = np.random.randn(10,30,5)
print(f"Q7: {q_7}\n{blank}")

##############################################################################################################

# Question 8 - Generate 10 elemented numPy array between -1 and 1
q_8 = np.random.randn(10)
print(f"Q8: {q_8}\n{blank}")

##############################################################################################################

# Question 9 - Generate a random matrix (3x5) between 10-50 
q_9 = (np.random.randint(10,50,15)).reshape(3,5)
print(f"Q9: {q_9}\n{blank}")

##############################################################################################################

# Question 10 - Calculate sum of matrix's columns and rows
q_10_row = np.sum(q_9, axis=1)
q_10_col = np.sum(q_9, axis=0)
print(f"Q10: Sum of lines: {q_10_row}\nSum of columns: {q_10_col}\n{blank}")

##############################################################################################################

# Question 11 - Find matrix's max, min and mean
q_11_max = np.max(q_9)
q_11_min = np.min(q_9)
q_11_average = np.mean(q_9)
print(f"Q11: Max of matrix: {q_11_max}\nMin of matrix: {q_11_min}\nAverage of matrix: {q_11_average}\n{blank}")

##############################################################################################################

# Question 12 - Find max variables index number
q_12 = np.argmax(q_9)
print(f"Q12: Index number of {q_11_max} is {q_12}\n{blank}")

##############################################################################################################

# Question 13 - Get first three elements of a numPy array which is between 10-20
q_13 = np.arange(10,20)
print(f"Q13: {(q_13)[:3]}\n{blank}")

##############################################################################################################

# Question 14 - Reverse Q13's array
q_14 = q_13[::-1]
print(f"Q14: {q_14}\n{blank}")

##############################################################################################################

# Question 15 - Get first line of matrix
q_15 = q_9[0]
print(f"Q15: {q_15}\n{blank}")

##############################################################################################################

# Question 16 - Get variables whic is at between 2nd line and 3rd column
q_16 = q_9[1, 2] # or [1, 2]
print(f"Q16: {q_16}\n{blank}")

##############################################################################################################

# Question 17 - Get only first variables in every line of matrix
q_17 = q_9[:, 0]
print(f"Q17: {q_17}\n{blank}")

##############################################################################################################

# Question 18 - Get every variable's power of 2 in matrix
q_18 = np.power(q_9, 2)
print(f"Q18: {q_18}\n{blank}")

##############################################################################################################

# Question 19 - Which one is positive in a numPy array which is between -50 and 50
q_19 = np.random.randint(-50,50,100)
q_19_r = q_19 >= 0
print(f"Q19: {q_19_r}\n{blank}")

##############################################################################################################