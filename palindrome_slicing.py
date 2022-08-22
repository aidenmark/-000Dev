# Aeriel Denmark
# List Slicing

# Write a program that determines whether a word entered by the user
# is a palindrome or not

word = str(raw_input("Enter a word: "))

if word == str(word)[::-1]:
	print("The given word is a palindrome")
else:
	print("The given word is a not a palindrome")
