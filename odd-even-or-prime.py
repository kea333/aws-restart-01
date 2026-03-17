# Python version:   3.7.16
# Encoding:         utf-8
# exe path:         /home/ec2-user/environment

# Write a simple script that takes integer input from user and determines if it is and od, even, or prime number

import math

myNumber = int(input("Please input any positive integer or whole number: "))

if myNumber % 2 != 0:
    print (f"{myNumber} is an odd number.")
else:
    print(f"{myNumber} is an even number.")

if (myNumber % 2 != 0) and (((6 * myNumber) + 1) % 2 != 0) or (myNumber % 2 != 0) and (((6 * myNumber) - 1) % 2 != 0) or myNumber in [1, 2, 3]:
    print(f"{myNumber} is a prime number.")
else:
    print("Sorted.")