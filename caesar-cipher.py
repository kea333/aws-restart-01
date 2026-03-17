# Python version:   3.7.16
# Encoding:         utf-8
# exe path:         /home/ec2-user/environment

"""
In programming, a function is a named section of a program that performs 
a specific task. Python has built-in functions like print() that are provided 
by the language. Additionally, you can use functions provided by other developers 
through the import statement. For example, you can use import math if you want to 
use the math.floor() function. In Python, you can make your own functions, 
which are called user-defined functions.
"""

# Using Functions to Implement a Caesar Cipher
"""
A Caesar cipher is a simple method of encryption that takes the letters of a 
message and shifts each letter along the alphabet by a certain number of places.
"""

# Create user-defined function that takes a string argument and concatenates with itself
def getDoubleAlphabet(alphabet):
    doubleAlphabet = alphabet + alphabet
    return doubleAlphabet

alphabet='ABC'

# Function call and output to console
print(getDoubleAlphabet(alphabet))

# Take input from user
def getMessage():
    stringToEncrypt = input("Please enter a message to encrypt: ")
    return stringToEncrypt


# Request cipher key from user
def getCipherKey():
    shiftAmount = input( "Please enter a key (whole number from 1-25): ")
    return shiftAmount

"""
Pseudocode algorithm for encryption:
1. Take three arguments: the message, the cipherKey, and the alphabet.
2. Initialize variables.
3. Use a for loop to traverse each letter in the message.
4. For a specific letter, find the position.
5. For a specific letter, determine the new position given the cipher key.
6. If current letter is in the alphabet, append the new letter to the encrypted message.
7. If current letter is not in the alphabet, append the current letter.
8. Return the encrypted message after exhausting all the letters in the message.
"""

# Encyption code
def encryptMessage(message, cipherKey, alphabet):
    encryptedMessage = ""
    uppercaseMessage = ""
    uppercaseMessage = message.upper()
    for currentCharacter in uppercaseMessage:
        position = alphabet.find(currentCharacter)
        newPosition = position + int(cipherKey)
        if currentCharacter in alphabet:
            encryptedMessage = encryptedMessage + alphabet[newPosition]
        else:
            encryptedMessage = encryptedMessage + currentCharacter
    return encryptedMessage

"""
Decrypting a message:
Functions are useful because you can reuse them. Write a decryptMessage() function by 
reusing the encryptMessage() function. For this simple encryption, you can undo the 
encryption by shifting each letter back. Thus, instead of adding the cipher key, 
you will subtract the cipher key. To avoid rewriting most of the logic, you will 
pass in a negative cipher key.
"""

# Decryption code
def decryptMessage(message, cipherKey, alphabet):
    decryptKey = -1 * int(cipherKey)
    return encryptMessage(message, decryptKey, alphabet)

# Create a main function, i.e. the main logic of the program
"""
Pseudocode plan of main logic:
1. Define a string variable to contain the English alphabet.
2. To be able to shift letters, double your alphabet string.
3. Get a message to encrypt from the user.
4. Get a cipher key from the user.
5. Encrypt the message.
6. Decrypt the message.
"""

# Main function
def runCaesarCipherProgram():
    myAlphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    print(f'Alphabet: {myAlphabet}')
    
    myAlphabet2 = getDoubleAlphabet(myAlphabet)
    print(f'Alphabet2: {myAlphabet2}')
    
    myMessage = getMessage()
    print(myMessage)
    
    myCipherKey = getCipherKey()
    print(myCipherKey)
    
    myEncryptedMessage = encryptMessage(myMessage, myCipherKey, myAlphabet2)
    print(f'Encrypted Message: {myEncryptedMessage}')
    
    myDecryptedMessage = decryptMessage(myEncryptedMessage, myCipherKey, myAlphabet2)
    print(f'Decypted Message: {myDecryptedMessage}')

# Function call
runCaesarCipherProgram()

"""
Output:
ABCABC
Alphabet: ABCDEFGHIJKLMNOPQRSTUVWXYZ
Alphabet2: ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ
Please enter a message to encrypt: Hello hello, how are you?
Hello hello, how are you?
Please enter a key (whole number from 1-25): 8
8
Encrypted Message: PMTTW PMTTW, PWE IZM GWC?
Decypted Message: HELLO HELLO, HOW ARE YOU?
"""
