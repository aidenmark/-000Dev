# Aeriel Denmark
# Prime Numbers

# Write a program that determines if the number entered by the user
# is a prime number or not

import math

num = int(raw_input("Enter a number: "))

if num > 1:
	for i in range (2, num):
		if (num % i) == 0:
			print(num, "is not a prime number")
			break
		else:
			print(num, "is a prime number")
			break
