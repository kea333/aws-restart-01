# Categorizing Values

# Creating a mixed-type list
# You can mix data types in a Python list. In other languages, this capability is not a feature of lists.
myMixedTypeList = [45, 290578, 1.02, True, "My dog is on the bed.", "45"]

# Use a for loop statement to traverse/iterate the list and print the data type for each item in the list
for item in myMixedTypeList:
    print("{} is of the data type {}".format(item,type(item)))