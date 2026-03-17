# Python 3.7.16 , 
# /home/ec2-user/environment
# encoding: UTF-8

# Working with the String Sequence and Numeric Weight of Insulin in Python

# Assign variables to the sequence elements of human insulin

# Store the human preproinsulin sequence in a variable called preproinsulin:
preproInsulin = "malwmrllpllallalwgpdpaaafvnqhlcgshlvealylvcgergffytpktr" \
"reaedlqvgqvelgggpgagslqplalegslqkrgiveqcctsicslyqlenycn"

"""
The PEP 8 (Python Enhancement Proposals 8) style guide recommends a maximum of 79 characters 
per line. PEPs are standards for Python best practices. A trailing backslash (\) in variable 
value is used to maintain compliance with the PEP8 style guide. Though the file still runs 
with longer line lengths, sticking to the suggested limit increases simplicity and readability. 
By using a backslash (\), you can split variables and code into smaller blocks, thereby 
maintaining the 79-character limit.
"""

# Store the remaining sequence elements of human insulin in variables:
lsInsulin = "malwmrllpllallalwgpdpaaa"
bInsulin = "fvnqhlcgshlvealylvcgergffytpkt"
aInsulin = "giveqcctsicslyqlenycn"
cInsulin = "rreaedlqvgqvelgggpgagslqplalegslqkr"

# Merge smaller insulin groupings into single insulin variable
insulin = bInsulin + aInsulin

# Printing "the sequence of human insulin" to console using successive print() commands:
print("The sequence of human preproinsulin:")
print(preproInsulin)

# Printing to console using concatenated strings inside the print function (one-liner):
print("The sequence of human insulin, chain a: " + aInsulin)

# Note: The built-in print() function accepts multiple arguments that can accomplish the same task in step 5. For example:
print("The sequence of human insulin, chain a:", aInsulin)

# Calculating the molecular weight of insulin  
# Creating a list of the amino acid (AA) weights  
aaWeights = {'A': 89.09, 'C': 121.16, 'D': 133.10, 'E': 147.13, 'F': 165.19,
'G': 75.07, 'H': 155.16, 'I': 131.17, 'K': 146.19, 'L': 131.17, 'M': 149.21,
'N': 132.12, 'P': 115.13, 'Q': 146.15, 'R': 174.20, 'S': 105.09, 'T': 119.12,
'V': 117.15, 'W': 204.23, 'Y': 181.19} 

# Count the number of each amino acids  
aaCountInsulin = ({x: float(insulin.upper().count(x)) for x in ['A', 'C',
'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T',
'V', 'W', 'Y']})  

# Multiply the count by the weights  
molecularWeightInsulin = sum({x: (aaCountInsulin[x]*aaWeights[x]) for x in
['A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R',
'S', 'T', 'V', 'W', 'Y']}.values())  

print("The rough molecular weight of insulin: " +
str(molecularWeightInsulin))

# The actual molecular weight of human insulin is 5807.63, but the program delivers 6696.42 because 
# it ignores certain bonds and post-translational processing
molecularWeightInsulinActual = 5807.63
print("Error percentage: " + str(((molecularWeightInsulin - molecularWeightInsulinActual)/molecularWeightInsulinActual)*100))

"""
Note: When you use string concatenation with floating point calculations, the print() function 
returns an error. This error is handled by a method called casting, which tells Python to use 
a certain data type. The previous use of the str() function is an example of casting.
"""
