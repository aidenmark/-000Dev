# Character Input
# Aeriel Denmark
# Wed 11/20/19

# www.practicepython.org

import math

name = str(raw_input("What is your name?  "))
age =  int(raw_input("How old are you?  "))
year = int(raw_input("What year is it?  "))
future = int((year - age)+1000)

print(name, "will be 1000 years old in the year", future)

# How do I get the quotation marks and commas to not appear 
# in the output?

# Sample Solution from site

# name = input("What is your name: ")
# age = int(input("How old are you: "))
# year = str((2014 - age)+100)
# print(name + " will be 100 years old in the year " + year)
