# BTK Academy
# Advanced Python Programming From Zero
# Lecture 5.2: Matplotlib - Forming a Graph
# python 5_2_figure.py
blank = "----------------------"

from turtle import width
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-10, 9, 20)
y= x ** 3
z = x ** 2

""" Graph inside Graph """
"""
figure = plt.figure()
axes_cube = figure.add_axes([0.1, 0.1, 0.8, 0.8]) # defines location of the figure
axes_cube.plot(x, y, 'b')
axes_cube.set_xlabel("X Axis")
axes_cube.set_ylabel("Y Axis")
axes_cube.set_title("Cubic")

axes_sqr = figure.add_axes([0.15, 0.6, 0.25, 0.25]) # (right, left, width, height)
axes_sqr.plot(x, z, 'r')
axes_sqr.set_xlabel("X Axis")
axes_sqr.set_ylabel("Y Axis")
axes_sqr.set_title("Square")
"""

""" Two values in a Graph """
"""
figure = plt.figure()
axes = figure.add_axes([0, 0, 1, 1]) 
axes.plot(x,z, label= "Square")
axes.plot(x,y, label= "Cubic")
axes.legend(loc=2) # left upper corner
"""

""" Seperate Graphs """
fig, axes = plt.subplots(nrows=2, ncols=1, figsize = (4,4))
axes[0].plot(x, y)
axes[0].set_title("Cubic")
axes[1].plot(x, z)
axes[1].set_title("Square")

plt.tight_layout()
fig.savefig("figure1.pdf")

plt.show()