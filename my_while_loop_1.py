# Working with Loops

# while loop
# A while loop makes a section of code repeat until a certain condition is met
import random   # Import dependency

# Inform the user about game
print("Welcome to Guess the Number!")
print("The rules are simple. I will think of a number, and you will try to guess it.")

# Generate a random number between 1 and 10
number = random.randint(1,10)

# Track whether the user guessed your number
isGuessRight = False

# Handle game logic
while isGuessRight != True:
    guess = input("Guess a number between 1 and 10: ")
    if int(guess) == number:
        print("You guessed {}. That is correct! You win!".format(guess))
        isGuessRight = True
    else:
        print("You guessed {}. Sorry, that isn’t it. Try again.".format(guess))
        
    """
    Note: The while loop will repeat the code inside the loop until the number is guessed correctly, 
    which is represented by the condition isGuessRight != True in the code.
    """

"""
Pseodocode:
1. If the user has not guessed the correct answer, enter the loop.
2. Ask the user for a guess.
3. Is the guess the correct number?
4. If the correct guess, tell the user it was the correct guess and exit the loop.
5. If the wrong guess, tell the user it was the wrong guess and continue the loop.
"""