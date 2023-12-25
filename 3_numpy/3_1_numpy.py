# BTK Academy
# Advanced Python Programming From Zero
# Lecture 3.1: NumPy - Data Analysis
# python 3_1_numpy.py
blank = "----------------------"

# NumPy 
# NumPy is a Python library used for working with arrays. 
# It also has functions for working in domain of linear algebra, fourier transform, and matrices.
# NumPy stands for Numerical Python.
import numpy as np


# Python List
py_list = [1,2,3,4,5,6,7,8,9]
print(type(py_list)) # <class 'list'>

# NumPy Array
np_array = np.array([1,2,3,4,5,6,7,8,9])
print(type(np_array)) # <class 'numpy.ndarray'>

py_multi = [[1,2,3],[4,5,6],[7,8,9]]
np_multi = np_array.reshape(3,3) # defining a matris 3x3 as py_multi
sum_line = np_multi.sum(axis=1) # brings sum of lines
sum_column = np_multi.sum(axis=0) # brings sum of columns


print(f"{py_multi}\n{blank}\n{np_multi}\n{blank}")
print(f"Dim of Array: {np_array.ndim}\n{blank}\nDim of Multi: {np_multi.ndim}\n{blank}")
print(f"Shape of Array: {np_array.shape}\n{blank}\nShape of Multi: {np_multi.shape}\n{blank}")

##############################################################################################################

# Working with numpy arrays

result_1 = np.arange(1,10) # generate an array between 1-10 and do not include 10
result_2 = np.arange(1,10,3) # generate an array between 1-10 and do not include 10 and increse by 3
result_3 = np.zeros(10) # generate 10 zeros as float
result_4 = np.ones(10) # generate 10 ones as float
result_5 = np.linspace(0,100,5) # generate an array between 0-100 and divide as 5 equal parts
result_6 = np.random.randint(0,10) # generates random number between 1-9 |randint(20) -> from zero to 19| as int
# result_6.max() get max
# result_6.min() get min
# result_6.mean() get mean
# result_6.argmax() get max number's index
result_7 = np.random.randint(0,20,3) # generates random number between 1-19 and get three of them as int
result_8 = np.random.randn(0,10,5) # generates random number between 1-9 and get five of them as float

print(f"{result_8}\n{blank}")

##############################################################################################################

# Indexing numpy array

numbers = np.array([10,20,30,40,50,60])
# numbers[5] -> fifth index
# numbers[-1] -> last index
# numbers[0:4] -> print between 0-4 (do not include 4)
# numbers[3:] -> print starting from 3 (include 3)
# numbers[:3] -> print until 3 (do not include 3rd)
# numbers[::] -> print whole
# numbers[::-1] -> reverse (60, 50, 40, 30, 20, 10)
# numbers[::-2] -> reverse as two (60, 40, 20)

numbers_2 = [[0,5,10],[15,20,25],[50,75,85]]
# result_9 = numbers_2[0] # prints [0, 5, 10]
# result_10 = numbers_2[2] # prints [50,75,85]
# result_11 = numbers_2[0, 2] # prints [10]
# result_12 = numbers_2[2, 1] # prints [75]
# result_13 = numbers_2[: , 2] # prints [10, 25, 85] | : means whole lines , 2 means 2nd indexed elements
# result_14 = numbers_2[: , 0] # prints [0, 15, 50] 
# result_15 = numbers_2[: , 0:2] # prints [[0,5], [15,20], [50,75]]
# result_16 = numbers_2[-1, :] # prints [50,75,85]
# result_17 = numbers_2[:2, :2] # prints [0,5], [15,25]

##############################################################################################################

# Numpy array operations

random_1 = np.random.randint(10,100,6)
random_2 = np.random.randint(10,100,6)
result_18 = random_1 + 10 # adds 10 to every element
result_19 = random_1 + random_2 # sum of them
result_20 = random_1 - random_2 # subtraction of them
result_21 = random_1 * random_2 # multiplication of them
result_22 = random_1 / random_2 # divison of them
result_23 = np.sin(random_1) # sin of random_1 variables
result_24 = np.cos(random_1) # cos of random_1 variables
result_25 = np.sqrt(random_1) # square of random_1 variables
result_26 = np.log(random_1) # log of random_1 variables

multi_num_1 = random_1.reshape(2,3)
multi_num_2 = random_2.reshape(2,3)

result_27 = np.vstack((multi_num_1, multi_num_2)) # turn as one matris (vertical stacking)
result_28 = np.hstack((multi_num_1, multi_num_2)) # turn as one matris (horizontal stacking)
result_29 = random_1 % 2 == 0 # controls every variables condition about %2 == 0 and returns boolean


print(f"{result_27}\n{blank}")
