# Working with Lists, Tuples, and Dictionaries

# Define a list by using square brackets
# A list has changeable members, i.e. it is mutable
myFruitList = ["apple", "banana", "cherry"]
print(myFruitList)
print(type(myFruitList))

# Accessing a list by position
print(myFruitList[0])
print(myFruitList[1])
print(myFruitList[2])

# Changing the values in a list
myFruitList[2] = "orange"
print(myFruitList)

# Introducing the tuple data type
# A tuple is like a list, but it can't be changed, i.e. immutable. Define a tuple by using parentheses i.e. normal brackets
myFinalAnswerTuple = ("apple", "banana", "pineapple")
print(myFinalAnswerTuple)
print(type(myFinalAnswerTuple))

# Accessing a tuple by position
print(myFinalAnswerTuple[0])
print(myFinalAnswerTuple[1])
print(myFinalAnswerTuple[2])

# Introducing the dictionary data type
# A dictionary is a list with named positions (keys) in a key-value format, defined by using curled brackets
myFavoriteFruitDictionary = {
  "Akua" : "apple",
  "Saanvi" : "banana",
  "Paulo" : "pineapple"
}

# Output to shell
print(myFavoriteFruitDictionary)

# Output data type to shell
print(type(myFavoriteFruitDictionary))

# Accessing a dictionary by name
print(myFavoriteFruitDictionary["Akua"])
print(myFavoriteFruitDictionary["Saanvi"])
print(myFavoriteFruitDictionary["Paulo"])