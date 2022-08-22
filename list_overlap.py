# Aeriel Denmark
# List Overlap

# Write a program that generates two list and returns a list
# that prints out the common elements from each list

import math
import random

a = [random.randrange(1, 100, 1) for i in range(5)]
b = [random.randrange(1, 100, 1) for i in range(10)]

print("a = ", str(a))
print("b = ", str(b))

if i in a and b:
	print(i)
else:
	print("There are no common elements between these two lists")
