# Python version:   3.7.16
# Encoding:         utf-8
# exe path:         /home/ec2-user/environment

# Locate jsonFileHandler.py Helper file for Lab 126: "Creating File Handlers and Modules for Retrieving Information about Insulin"
# Rubric 14 - File Handler in Python Programming - Week 5
import os
import sys

filename = "jsonFileHandler.py"
search_path = "/home/ec2-user/environment"
found = False

# Recursive search through the file tree
for root, dirs, files in os.walk(search_path):
    if filename in files:
        print(f"✅ Found at: {os.path.join(root, filename)}")
        found = True

if not found:
    print(f"❌ '{filename}' not found in {search_path}")

# Check if the current directory is in the Python path
print(f"\nCurrent Working Directory: {os.getcwd()}")
print(f"Is CWD in sys.path? {'Yes' if '' in sys.path or os.getcwd() in sys.path else 'No'}")

"""
Output:
❌ 'jsonFileHandler.py' not found in /home/ec2-user/environment

Current Working Directory: /home/ec2-user/environment
Is CWD in sys.path? Yes
"""

