# Python version:   3.7.16
# Encoding:         utf-8
# exe path:         /home/ec2-user/environment

# Module Lab: Caesar Cipher Program Bug #1
#
# In a previous lab, you created a Caesar cipher program. This version of
# the program is buggy. Use a debugger to find the bug and fix it.

# Double the given alphabet
def getDoubleAlphabet(alphabet):
    doubleAlphabet = alphabet + alphabet
    return doubleAlphabet

# Get a message to encrypt
def getMessage():
    stringToEncrypt = input("Please enter a message to encrypt: ")
    return stringToEncrypt

# Get a cipher key
def getCipherKey():
    shiftAmount = input("Please enter a key (whole number from 1-25): ")
    return shiftAmount

# Encrypt message
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

# Decrypt message
def decryptMessage(message, cipherKey, alphabet):
    decryptKey = -1 * int(cipherKey)
    return encryptMessage(message, decryptKey, alphabet)

# Main program logic
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
    print(f'Decrypted Message: {myDecryptedMessage}')

# Main logic
runCaesarCipherProgram()

"""
Output:
Alphabet: ABCDEFGHIJKLMNOPQRSTUVWXYZ
Alphabet2: ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ
Please enter a message to encrypt: Good morning.
Good morning.
Please enter a key (whole number from 1-25): 3
3
Traceback (most recent call last):
  File "/home/ec2-user/environment/debug-caesar-1.py", line 60, in <module>
    runCaesarCipherProgram()
  File "/home/ec2-user/environment/debug-caesar-1.py", line 54, in runCaesarCipherProgram
    myEncryptedMessage = encryptMessage(myMessage, myCipherKey, myAlphabet2)
  File "/home/ec2-user/environment/debug-caesar-1.py", line 32, in encryptMessage
    newPosition = position + cipherKey
TypeError: unsupported operand type(s) for +: 'int' and 'str'
"""

# The program ends in a traceback. A traceback is a stack trace that starts from the point of an exception handler. 
# It then goes down the call chain to the point where the exception was raised. In other words, an error occurred.

# Using the debugger to find and fix the bug in the first lab file for the buggy Caesar cipher.

"""
Q1: When do you use 'stepover' (ignore??) in right pane, and when do you use 'resume' (continue to interprete??) in right pane?
Q2: Is it because no variables are hard coded that WATCH EXPRESSIONS throw bizzaire values in this Lab? Why have the WATCH EXPRESSIONS I specified vanished on their own accord?
Q3: Another run with different WATCH EXPRESSIONS, 'stringToEncrypt: No value', and 'shiftAmount: NameError-not specified'
Q4: Exit message "Program terminated with no exit value" doesn't seem right, should it not terminate with code 0?
"""