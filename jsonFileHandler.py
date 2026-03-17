# Python version:   3.7.16
# Encoding:         utf-8
# exe path:         /home/ec2-user/environment

# Creating File Handlers and Modules for Retrieving Information about Insulin

# Create JSON file handler module
import json

# Function to read JSON file
def readJsonFile(fileName):
    data=""
    try:
        with open(fileName) as json_file:
            data = json.load(json_file)
    except IOError:
        print("Could not read file")
    return data
    
