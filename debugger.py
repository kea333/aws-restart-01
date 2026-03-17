# Python version:   3.7.16
# Encoding:         utf-8
# exe path:         /home/ec2-user/environment

# Using the Debugger
# The Python Debugger (pdb) is an interactive source code debugger for Python programs
# Cloud9 offers an interactive source code debugger for several languages, including Python.

name = "John"
print("Hello " + name + ".")
age = 40
print(name + " is " + str(age) + " years old.")

"""
To use debugger in AWS Cloud9: 
1. Click debugger icon on right pane to expand pane
2. Select breakpoints in your code - breakpoints show up under BREAKPOINTS in right pane
3. Pull up bottom pane (if absent) and click '+'
4. Select New Run Configuration - new pane window shows up
5. Click debugger icon to run in debugger mode
6. Click 'Run'
7. Fix each bug thrown up and click Restart icon
"""