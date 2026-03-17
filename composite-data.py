# Working with Composite Data Types

# Create car inventory program
# Define the dictionary
import csv
import copy

myVehicle = {
    "vin" : "<empty>",
    "make" : "<empty>" ,
    "model" : "<empty>" ,
    "year" : 0,
    "range" : 0,
    "topSpeed" : 0,
    "zeroSixty" : 0.0,
    "mileage" : 0
}

# Use a for loop to iterate over the initial keys and values of the dictionary
for key, value in myVehicle.items():         # Note: The items() function belongs to the dictionary data type. The items() function
    print("{} : {}".format(key,value))      # tells the for loop to traverse the collection owned by the dictionary data type
    
# Define an empty list to hold the car inventory that will be read
myInventoryList = []

# Copy the CSV file into memory
with open('car_fleet.csv') as csvFile:
    csvReader = csv.reader(csvFile, delimiter=',')  
    lineCount = 0  
    for row in csvReader:
        if lineCount == 0:
            print(f'Column names are: {", ".join(row)}')  
            lineCount += 1  
        else:  
            print(f'vin: {row[0]} make: {row[1]}, model: {row[2]}, year: {row[3]}, range: {row[4]}, topSpeed: {row[5]}, zeroSixty: {row[6]}, mileage: {row[7]}')  
            currentVehicle = copy.deepcopy(myVehicle)  # This line makes sure that new storage boxes are created in memory to store the new tabular data that is being read
            currentVehicle["vin"] = row[0]  
            currentVehicle["make"] = row[1]  
            currentVehicle["model"] = row[2]  
            currentVehicle["year"] = row[3]  
            currentVehicle["range"] = row[4]  
            currentVehicle["topSpeed"] = row[5]  
            currentVehicle["zeroSixty"] = row[6]  
            currentVehicle["mileage"] = row[7]  
            myInventoryList.append(currentVehicle)  
            lineCount += 1  
            
    print(f'Processed {lineCount} lines.')

# Print car inventory from the myInventoryList variable
for myCarProperties in myInventoryList:
    for key, value in myCarProperties.items():
        print("{} : {}".format(key,value))
        print("-----")

"""
Debugging steps

1. error={
venv dependency is missing
venv and ensurepip are required to create virtual environment. Please install python3-venv and try again
    
}

This error occurs because the version of Python installed on your AWS Cloud9 EC2 instance is missing the necessary modules to create virtual environments, which Cloud9 uses for various internal and user-defined tasks. 
To resolve this, follow these steps based on the operating system of your Cloud9 environment:

Identify Your Environment OS
Check which Linux distribution your Cloud9 instance is running with this command in the Cloud9 terminal:

cat /etc/os-release

output says Amazon Linux version 2

comand: sudo yum update -y

output says Dependencies resolved, updated, success.

command: sudo yum install -y python3

output says Dependency inatalled, Complete!

python --version, output Python 3.7.16

command: python3 -m venv test-env

output: ['apple', 'banana', 'cherry']
<class 'list'>
apple
banana
cherry
['apple', 'banana', 'orange']
('apple', 'banana', 'pineapple')
<class 'tuple'>
...
...
Could not import runpy module
Traceback (most recent call last):
  File "/usr/lib64/python3.7/runpy.py", line 15, in <module>
    import importlib.util
  File "/usr/lib64/python3.7/importlib/util.py", line 14, in <module>
    from contextlib import contextmanager
  File "/usr/lib64/python3.7/contextlib.py", line 5, in <module>
    from collections import deque
ImportError: cannot import name 'deque' from 'collections' (/home/ec2-user/environment/collections.py)

The issue is one of a a "naming collision." The error ImportError: cannot import name 'deque' from 
'collections' is happening because you created a file named collections.py in your environment folder.
When Python tries to run the venv module, it looks for the built-in collections library. Instead of 
finding the system library, it is finding your file (/home/ec2-user/environment/collections.py), 
which doesn't contain the required deque function.

2. Step-by-Step Fix
Rename local file:
Change the name of local script so it doesn't conflict with Python's standard library. Run this in Cloud9 terminal:

mv /home/ec2-user/environment/collections.py /home/ec2-user/environment/my_collections_practice.py

Then Remove any compiled cache:
Python may have created a __pycache__ folder or a .pyc file for your old script. Clear it out to be safe:

rm -rf /home/ec2-user/environment/__pycache__

Why this happened
Python searches for modules in the current working directory first. By naming your practice file collections.py, 
you "shadowed" the Python Standard Library collections module. This broke internal Python functions (like contextlib) 
that rely on the real collections module.

Pro-tip: Avoid naming your scripts after common libraries (e.g., test.py, json.py, sys.py, or collections.py).

3. error={
/usr/bin/python3: No module named ikp3db

    To use python debugger install ikpdb by running: 
        sudo pip3 install ikp3db
}

This error occurs because the AWS Cloud9 Python Debugger depends on the ikp3db module, which is not pre-installed 
in your current Python environment or virtual environment. 

Follow these steps to install the missing dependency:
1. Identify Your Active Environment

Since you deleted the test-env and are working directly in ~/environment, you are using the System Python environment. 
To get the Cloud9 debugger working globally on your instance, follow these steps:

Install the Debugger Module (Global)
Run the installation with sudo to ensure the system-wide Python can access the debugger:

sudo pip3 install ikp3db

Handle Potential Build Errors
If the installation fails with an error about Python.h or gcc, you need the Python development headers. 
Run the command matching your OS: For Amazon Linux 2 / 2023:

sudo yum install python3-devel -y

Verify the Fix
Run your script again using the Run button in the Cloud9 IDE or via the terminal. 
To verify the module is correctly mapped globally, run:

python3 -c "import ikp3db; print('Debugger module ready')"

Why this happened
AWS Cloud9 uses the ikp3db library to bridge your code with the graphical Debugger 
panel (where you set breakpoints and watch variables). Without this library, the IDE 
cannot "talk" to your running script to pause it or inspect data.

Running the above "sudo pip3 install ikp3db" produced the following error:

error={
...
...
ERROR: Command errored out with exit status 1:
...
...
directory
     #include "Python.h"
              ^~~~~~~~~~
    compilation terminated.
...
...
}

The error fatal error: Python.h: No such file or directory confirms that your system is missing 
the Python development headers. These are required whenever pip tries to compile a C-extension 
(like ikp3db) from source.
Here is the step-by-step fix for your specific environment (which is running Python 3.7 on Amazon Linux):
1. Install Python 3.7 Development Headers
Run the command to provide the compiler with the Python.h file it’s looking for:

sudo yum install python3-devel -y

sudo pip3 install ikp3db

output: "WARNING: Running pip install with root privileges is generally not a good idea. 
Try `pip3 install --user` instead."

To fix the missing headers while also addressing the root privileges warning, we will install 
the package to your user directory rather than the system folders. This satisfies the 
security warning and keeps your environment clean.

Install the Required Headers
You still need the sudo command for this step because you are modifying system-level compilers, 
but this is perfectly safe:

sudo yum install python3-devel -y

Install the Debugger to the User Space
Instead of using sudo pip3, use the --user flag. This installs the package to ~/.local, 
which doesn't require root privileges and stops the warning:

pip3 install --user ikp3db

Note: If you see a warning about the "script path not being in PATH," you can safely 
ignore it for now as the IDE knows where to look.

Verify Without Root
Confirm that your standard user can now see and use the module:

python3 -c "import ikp3db; print('Debugger successfully installed in user space!')"

Why this is the "Best Practice" path:
Security: Using --user means you aren't letting a third-party script from pip modify your system core.
Stability: Your Cloud9 environment remains stable because you aren't overwriting system files.
No Warnings: The annoying "Running pip as root" message will disappear for this and future installs.

the above "python3 -c "import ikp3db; print('Debugger successfully installed in user space!')" " step 
produces the error "bash: !': event not found".

That error is actually a Bash shell error, not a Python one. In Bash, the exclamation mark (!) is a 
special character used for "history expansion." When you put it inside double quotes, 
Bash tries to find a previous command that matches it and fails. GNU Bash Manual - History Expansion
Here are two ways to fix the command:
Option 1: Use Single Quotes (Recommended)
Bash does not try to interpret characters inside single quotes, so the exclamation mark won't cause trouble.

python3 -c 'import ikp3db; print("Debugger successfully installed in user space!")'

Option 2: Escape the Exclamation Mark
If you prefer double quotes, you can put a backslash before the !.

python3 -c "import ikp3db; print('Debugger successfully installed in user space\!')"

Next Step
Once you run the command and see the success message, your Cloud9 Debugger should be fully 
functional. Try setting a breakpoint (click the margin to the left of a line number so a 
red dot appears) and click the Run button.
"""