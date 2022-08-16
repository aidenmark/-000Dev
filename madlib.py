# Aeriel Denmark
# August 2022

# The following program is a MadLib generator.

# The program will prompt the user for an input that will then be assigned to a variable.
# The variables will be concated together to form a story based on the inputs from the user.

first_name = input("Enter a first name: ")
last_name = input("Enter a last name: ")
age = input("Enter an age: ")
color = input("Enter a color: ")
candy = input("Enter favorite candy: ")
activity = input("Enter favorite activity: ")

print("Hi! My name is " + first_name.capitalize(), last_name.capitalize() + ". I am " +
        age, "years old and my favorite color is", color + ". My favorite candy is " +
        candy, "and I enjoy " + activity + ".")
