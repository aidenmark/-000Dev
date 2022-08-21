# Aeriel Denmark

# Technical interview question

import math

myArray = range(1,16)

print(myArray)

for i in myArray:
	if  i % 3 == 0 and i % 5 == 0:
		print("Merry Christmas")
	elif i % 5 == 0:
		print("Christmas")
	elif i % 3 == 0:  # The num '15' should print 'Merry Christmas'
		print("Merry") # but it only prints 'Merry'
	else:
		print(i)
