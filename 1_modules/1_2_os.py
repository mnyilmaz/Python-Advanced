# BTK Academy
# Advanced Python Programming From Zero
# Lecture 1.2: Os Module in Python 
# python 1_2_os.py
blank = "----------------------"

# Os Module
# The OS module in Python provides functions for interacting with the operating system.
import os

result = os.name # gives "nt" as result beacuse of windows
print(result)
print(blank)

# Finding out which directory we're using at the moment
cwd = os.getcwd() # "\2_advanced_python" - gives the loaction of folder
print(cwd)
print(blank)

##############################################################################################################

# Generate a new folder in a current directory
# os.mkdir("newdirectory") # generates a new folder
# os.rename("newdirectory", "notnewdirectory") # changing folder name
# os.remove("newdirectory") # removes folder
# os.removedirs("newdirectory") # also removes subfolders

##############################################################################################################

# Generate more than a folder
# os.makedirs("newnewdirectory/newnewnewdirectory")
# You may specify the location while using os.makedir()

##############################################################################################################

# Changing Directory
# os.chdir("M:\\") # makes directory as c
# os.chdir("..") works as cd ..
# os.chdir("../..") works as double cd .. 

##############################################################################################################

# Listing
listing = os.listdir()
print(listing)
print(blank)

for folder in os.listdir():
    if folder.endswith(".py"):
        print(folder)

print(blank)

##############################################################################################################

import datetime
info = os.stat("1_1_datetime.py")
gd = datetime.datetime.fromtimestamp(info.st_atime) # generation date
# cd = datetime.datetime.fromtimestamp(info.st_ctime) -> last access date
# md = datetime.datetime.fromtimestamp(info.st_mtime) -> last modification date

print(f"Info for the datetime file: {info}")
print(blank)
print(f"Normalized datetime{gd}")
print(blank)

##############################################################################################################

# Opening a program
# os.system("notepad.exe")

##############################################################################################################

# Path
path = os.path.abspath("1_1_datetime.py")
print(path)
print(blank)

# dirpath = os.path.dirname("/2_advanced_python/1_2_os.py")
dirpath = os.path.dirname("M://uncharted.jpg")
print(dirpath)
print(blank)

# Actual usage of path
actual = os.path.dirname(os.path.abspath("uncharted.jpg"))
print(actual)
print(blank)

# Exists
exists = os.path.exists("M://")
print(f"File existence situation is {exists}")
print(blank)

# Is file or directory
is_dir = os.path.isdir("M://")
print(is_dir)
is_file = os.path.isdir("M://")
print(is_file)
print(blank)

# Join and Split
join = os.path.join("M://new", "new2")
print(join)
split = os.path.splitext("1_1_datetime.py")
print(split)
print(blank)

##############################################################################################################


