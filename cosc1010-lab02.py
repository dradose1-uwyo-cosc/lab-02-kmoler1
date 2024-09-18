# Kaleb Moler
# UWYO COSC 1010
# 9/18/24
# Lab 02 
# Lab Section: 15
# Sources, people worked with, help given to: 
# https://www.online-python.com/ (online IDE)
# Jay Trujio, Jhett Carr

mascot = "cowboy joe"

## Section ONE

# Complete the following print statement to print out "Hello, COSC1010"
print("Hello, COSC1010")

# Assign the string above to a variable named hello_message and print that variable
hello_message = "Hello, COSC101"
print(hello_message)

# Assign the string "cowboy joe" to a variable, and print that variable with title casing
print(mascot.title())

# Complete the following f-string print message 
    # You will need to create your own variables and insert them  
    # the final message should read `The University of Wyoming was founded in 1886`
school="university of wyoming"
year=1886

print(f"The {school.title()} was founded in {str(year)}")

# Now let's do some math with variables 
    # Create two variables x and y and assign them the values 5 and 10 respectively 
    # Complete the following print statements using your variables
    #All math must be done within the braces in the f-strings
x=int(5)
y=int(10)
print(f"x + y = {x+y}")
print(f"x - y = {x-y}")
print(f"x * y = {x*y}")
print(f"x / y = {x/y}")

# String concatenation 
    # Finally we will take a look at string concatenation
    # String concatenation combines two strings together
    # It is done using the + operator
    # Create three variables:
        # first_name, which is your first name 
first_name=input("What is your first name: ").strip()

        # last_name, which is your last name
last_name=input("What is your last name: ").strip()
        # space, which is a space character 
space= " "
    # Use string concatenation to print out your full name 
print(first_name.title()+space+last_name.title())
