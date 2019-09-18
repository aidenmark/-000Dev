# Aeriel Denmark
# Jonny Dailey
# #000Dev
# Tues 9/17/2019

import os

# Use path.expander to expand the inital path of the user's home directory

path = os.path.expanduser("~/Desktop")

# Change the user's directory to their Desktop

os.chdir(path)

# Create a new directory (folder) on the user's Desktop

os.mkdir("Wakanda Forever")

# Create a path that navigates to the newly created directory

path = os.path.expanduser("~/Desktop/Wakanda Forever")

os.chdir(path)

# Create a file to write to in the newly created directory

f= open("index.html", "w+")

# Write the current time to the third line of the file

import datetime

currentDT = datetime.datetime.now()

f.write("currentDT")



