# Working with the String Data Type
myString = "This is a string."
print(myString)

# Get data type
print(type(myString))

# Convert the return value of type into a string
print(myString + " is of the data type " + str(type(myString)))

# String concatenation
firstString = "water"
secondString = "fall"
thirdString = firstString + secondString
print(thirdString)

# Working with input strings
# The input() function will pause the code until a user enters a string and presses ENTER
name = input("What is your name? ")
print(name)

# Formatting output strings
color = input("What is your favorite color?  ")
animal = input("What is your favorite animal?  ")

print("{}, you like a {} {}!".format(name,color,animal))