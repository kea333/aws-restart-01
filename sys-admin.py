# Python version:   3.7.16
# Encoding:         utf-8
# exe path:         /home/ec2-user/environment

# Introducing System Administration with Python
"""
You can use Linux to do many administrative tasks from the terminal, or the Bash command line. 
Python provides several modules that you can also use to run commands on the command line. 
In this lab, we use os.system() and subprocess.run() to run Bash commands from Python.
"""

# Import dependency
import os

# Use .system() module, which takes a string argument, to run bash shell commands from python file
os.system("ls")

"""
Output:
ainsulin-seq-clean.txt   my_collections_practice.py
analyse-insulin-1.py     my_conditionals_practice.py
binsulin-seq-clean.txt   my_for_loop_1.py
caesar-cipher.py         my_while_loop_1.py
calc_weight_json.py      net-charge.py
car_fleet.csv            numeric-data.py
categorize-values.py     preproinsulin-seq-clean.txt
cinsulin-seq-clean.txt   preproinsulin-seq.txt
composite-data.py        README.md
files                    searchHelperFile-1.py
hello-world.py           string-data-type.py
jsonFileHandler.py       string-insulin.py
lsinsulin-seq-clean.txt  sys-admin.py
"""

# Using subprocess.run()
"""
You can use the subprocess module to spawn new processes, connect to input/output/error pipes, 
and obtain error codes. The subprocess.run() function can take many new arguments, 
but those additional arguments are optional. The subprocess.run() function is powerful because 
you can use it to run any Bash command.

The full list of arguments for subprocess.run() looks like the following list:

subprocess.run(args, *, stdin=None, input=None, stdout=None, stderr=None, capture_output=False, 
shell=False, cwd=None, timeout=None, check=False, encoding=None, errors=None, text=None, env=None, 
universal_newlines=None)
"""

import subprocess
subprocess.run(["ls"]) # Same output as above

# In Python, square brackets are list data types, which means that run() can take a list of arguments.
subprocess.run(["ls","-l"]) # "-l" is an argument that tells the ls command to use a long-listing format

"""
Output:
total 108
-rw-r--r-- 1 ec2-user ec2-user   21 Feb  1 04:36 ainsulin-seq-clean.txt
-rw-r--r-- 1 ec2-user ec2-user 1260 Feb  1 04:36 analyse-insulin-1.py
-rw-r--r-- 1 ec2-user ec2-user   30 Feb  1 04:15 binsulin-seq-clean.txt
-rw-r--r-- 1 ec2-user ec2-user 3982 Feb  1 23:06 caesar-cipher.py
-rw-r--r-- 1 ec2-user ec2-user 1775 Feb  2 00:36 calc_weight_json.py
-rw-r--r-- 1 ec2-user ec2-user  295 Jan 31 21:45 car_fleet.csv
-rw-r--r-- 1 ec2-user ec2-user  430 Jan 31 21:21 categorize-values.py
-rw-r--r-- 1 ec2-user ec2-user   35 Feb  1 04:25 cinsulin-seq-clean.txt
-rw-r--r-- 1 ec2-user ec2-user 9732 Feb  1 01:15 composite-data.py
drwxr-xr-x 2 ec2-user ec2-user   26 Feb  1 23:30 files
-rw-r--r-- 1 ec2-user ec2-user   42 Jan 31 19:28 hello-world.py
-rw-r--r-- 1 ec2-user ec2-user  465 Feb  2 00:28 jsonFileHandler.py
-rw-r--r-- 1 ec2-user ec2-user   24 Feb  1 04:05 lsinsulin-seq-clean.txt
-rw-r--r-- 1 ec2-user ec2-user 1323 Jan 31 20:18 my_collections_practice.py
-rw-r--r-- 1 ec2-user ec2-user 1009 Feb  1 01:54 my_conditionals_practice.py
-rw-r--r-- 1 ec2-user ec2-user  587 Feb  1 02:37 my_for_loop_1.py
-rw-r--r-- 1 ec2-user ec2-user 1294 Feb  1 02:21 my_while_loop_1.py
-rw-r--r-- 1 ec2-user ec2-user 1620 Feb  1 21:45 net-charge.py
-rw-r--r-- 1 ec2-user ec2-user  844 Jan 31 19:09 numeric-data.py
-rw-r--r-- 1 ec2-user ec2-user  110 Feb  1 03:42 preproinsulin-seq-clean.txt
-rw-r--r-- 1 ec2-user ec2-user  156 Feb  1 03:42 preproinsulin-seq.txt
-rw-r--r-- 1 ec2-user ec2-user  569 Dec  9 21:16 README.md
-rw-r--r-- 1 ec2-user ec2-user 1037 Feb  2 00:09 searchHelperFile-1.py
-rw-r--r-- 1 ec2-user ec2-user  716 Jan 31 19:45 string-data-type.py
-rw-r--r-- 1 ec2-user ec2-user 3254 Feb  1 20:56 string-insulin.py
-rw-r--r-- 1 ec2-user ec2-user 2010 Feb  2 10:19 sys-admin.py
"""

# Run with 3 arguments
print("\n")
subprocess.run(["ls","-l","README.md"])

"""
Output:
-rw-r--r-- 1 ec2-user ec2-user 569 Dec  9 21:16 README.md
"""

# Retrieve system information by calling the 'uname' command to get system information
command="uname"
commandArgument="-a"
print(f'Gathering system information with command: {command} {commandArgument}')
subprocess.run([command,commandArgument])

"""
Output:
Gathering system information with command: uname -a
Linux ip-10-16-10-124.us-west-2.compute.internal 5.10.247-246.989.amzn2.x86_64 #1 SMP Fri Dec 19 00:41:58 UTC 2025 x86_64 x86_64 x86_64 GNU/Linux
"""

# Retrieve information about disk space using  the 'df' command
command="ps"
commandArgument="-x"
print("\n")
print(f'Gathering active process information with command: {command} {commandArgument}')
subprocess.run([command,commandArgument])

"""
Output:
Gathering active process information with command: ps -x
  PID TTY      STAT   TIME COMMAND
  305 ?        S      0:00 bash -c #!/usr/bin/env bash # Helper script to launch
  317 ?        Sl     0:00 /home/ec2-user/.c9/python3/bin/python3 -c import argp
  324 ?        S      0:00 /home/ec2-user/.c9/python3/bin/python3 /home/ec2-user
  388 pts/3    Ss+    0:00 bash -l -c trap 'printf "\e[01;30m\n\nProcess exited 
  405 pts/3    S+     0:00 python3 /home/ec2-user/environment/sys-admin.py
  411 pts/3    R+     0:00 ps -x
 3262 ?        S      0:00 sshd: ec2-user@notty
 3263 ?        Ss     0:00 bash --noprofile --norc
 3264 ?        Sl     0:10 vfs-worker {"pingInterval":5000,"nodePath":"/home/ec2
 3583 ?        Ssl    0:04 /opt/c9/dependencies/node22-linux-x64/601a730becaeae2
 3626 ?        S      0:00 sshd: ec2-user@notty
 3629 ?        Ss     0:00 bash --noprofile --norc
 3635 ?        Sl     0:00 vfs-worker {"pingInterval":5000,"nodePath":"/home/ec2
 3696 pts/0    Ss+    0:00 /home/ec2-user/.c9/bin/tmux -u2 -L cloud92.2 new -s o
 3699 ?        Rs     0:00 /home/ec2-user/.c9/bin/tmux -u2 -L cloud92.2 new -s o
 3767 ?        Sl     0:00 /opt/c9/dependencies/node22-linux-x64/601a730becaeae2
 3774 ?        Sl     0:00 /opt/c9/dependencies/node22-linux-x64/601a730becaeae2
 5275 pts/1    Ss+    0:00 /home/ec2-user/.c9/bin/tmux -u2 -L cloud92.2 new -s c
 5277 pts/2    Ss     0:00 bash -c export ISOUTPUTPANE=0;bash -l
 5278 pts/2    S+     0:00 bash -l
"""
