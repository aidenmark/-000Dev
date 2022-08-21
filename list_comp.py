# Aeriel Denmark
# List Comprehension

# Write a program that creates a list and then makes a new list that
# only lists the even elements of the original list

import random

a = [random.randrange(1, 100, 1) for i in range(10)]

print("a = ", str(a))

for i in a:
	if i % 2 == 0:
		print(i)
