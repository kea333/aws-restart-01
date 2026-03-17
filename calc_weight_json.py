# Python version:   3.7.16
# Encoding:         utf-8
# exe path:         /home/ec2-user/environment

# Creating File Handlers and Modules for Retrieving Information about Insulin

# Create the main program
# Main program that parses the JSON data and calculates the molecular weight as in a previous lab

# Import the jsonFileHandle module
import jsonFileHandler

# Retrieve the JSON data and store it in a data variable
data = jsonFileHandler.readJsonFile('files/insulin.json')

# Test if the returned data is not empty and obtain the insulin data
if data != "" :
    bInsulin = data['molecules']['bInsulin']
    aInsulin = data['molecules']['aInsulin']
    insulin = bInsulin + aInsulin
    molecularWeightInsulinActual = data['molecularWeightInsulinActual']
    print('bInsulin: ' + bInsulin)
    print('aInsulin: ' + aInsulin)
    print('molecularWeightInsulinActual: ' + str(molecularWeightInsulinActual))
    
    # Calculating the molecular weight of insulin  
    # Getting a list of the amino acid (AA) weights  
    aaWeights = data['weights']
    # Count the number of each amino acids  
    aaCountInsulin = ({x: float(insulin.upper().count(x)) for x in ['A','C','D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R','S', 'T','V', 'W', 'Y']})  
    # Multiply the count by the weights  
    molecularWeightInsulin = sum({x: (aaCountInsulin[x]*aaWeights[x]) for x in
    ['A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R','S', 'T', 'V', 'W', 'Y']}.values())  
    print("The rough molecular weight of insulin: " +
    str(molecularWeightInsulin))
    print("Percent error: " + str(((molecularWeightInsulin - molecularWeightInsulinActual)/molecularWeightInsulinActual)*100))
    
else:
    print("Error. Exiting program")
    
"""
Output:
bInsulin: fvnqhlcgshlvealylvcgergffytpkt
aInsulin: giveqcctsicslyqlenycn
molecularWeightInsulinActual: 5807.63
The rough molecular weight of insulin: 6696.42
Percent error: 15.303833060990454
"""