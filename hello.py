# The following is a function that defines the paramaters of 'say_hello'
def say_hello(myParam):
    print("Hello, {}World" .format(myParam))
# {} is a placeholder for some number that will appear when the function
# is called later on

# Create a for loop with a set range   
for i in range(5):
    say_hello(i+1)
# This calls the previously defined function and add 1 to it