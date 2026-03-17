# Python3.7.16
# Coding: utf-8  
# Store the human preproinsulin sequence in a variable called preproinsulin:  
preproInsulin = "malwmrllpllallalwgpdpaaafvnqhlcgshlvealylvcgergffytpktrreaedlqvgqvelgggpgagslqplalegslqkrgiveqcctsicslyqlenycn"  
# Store the remaining sequence elements of human insulin in variables:  
lsInsulin = "malwmrllpllallalwgpdpaaa"  
bInsulin = "fvnqhlcgshlvealylvcgergffytpkt"  
aInsulin = "giveqcctsicslyqlenycn"  
cInsulin = "rreaedlqvgqvelgggpgagslqplalegslqkr"  
insulin = bInsulin + aInsulin

# New dictionary
pKR = {'y':10.07,'c': 8.18,'k':10.53,'h':6.00,'r':12.48,'d':3.65,'e':4.25}
      # Note: Y, C, K, H, R, D, and E are the only amino acids that contribute to the net-charge calculation

# Use count() to count the numbers of each amino acid
"""
1. To see how many amino acids in insulin are Y, use the count() method by entering: insulin.count("Y")
2. Next, update the insulin.count() line by casting the variable returned by the count() method as a float: float(insulin.count("Y"))
3. Use this method to find all entities from a list. This process can be done by using list comprehension
"""

# Use list comprehension
seqCount = ({x: float(insulin.count(x)) for x in ['y','c','k','h','r','d','e']})

# Write the net charge formula
pH = 0 

while (pH <= 14):
    netCharge = (
        +(sum({x: ((seqCount[x]*(10**pKR[x]))/((10**pH)+(10**pKR[x]))) \
        for x in ['k','h','r']}.values()))
        -(sum({x: ((seqCount[x]*(10**pH))/((10**pH)+(10**pKR[x]))) \
        for x in ['y','c','d','e']}.values()))
    )
    
    print('{0:.2f}'.format(pH), netCharge)
    
    pH +=1
    