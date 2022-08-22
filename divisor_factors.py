# Aeriel Denmark
# Divisor Factor

# Write a program that prints out all factors of the
# number given by the user

import math
import random

def factors(x):
	print('The factors of', x, 'are: ')
	for i in range(1, x + 1):
		if x % i == 0:
			print(i)


num = int(raw_input("Enter a number: "))

factors(num)
