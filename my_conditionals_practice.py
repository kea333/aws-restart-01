# Working with Conditionals

userReply = input("Do you need to ship a package? (Enter yes or no) ")  # Get information from the user

# the if statement
if userReply == "yes":
    print("We can help you ship that package!")

# the else statement
else:
    print("Please come back when you need to ship a package. Thank you.")

# the elif statement
userReply = input("Would you like to buy stamps, buy an envelope, or make a copy? (Enter stamps, envelope, or copy) ")
if userReply == "stamps":
    print("We have many stamp designs to choose from.")
elif userReply == "envelope":
    print("We have many envelope sizes to choose from.")
elif userReply == "copy":
    copies = input("How many copies would you like? (Enter a number) ")
    print("Here are {} copies.".format(copies))
else:
    print("Thank you, please come again.")

"""
Note: The if, elif, and else statements allow only one path to run at a time. 
The program doesn’t check the other statements after it finds a condition that is true.
"""
