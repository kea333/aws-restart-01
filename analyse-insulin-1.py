# Count number of amino acid letters
print(len("malwmrllpllallalwgpdpaaafvnqhlcgshlvealylvcgergffytpktrreaedlqvgqvelgggpgagslqplalegslqkrgiveqcctsicslyqlenycn"))

# Assign full amino acid sequence to variable
full_amino_acid_sequence = "malwmrllpllallalwgpdpaaafvnqhlcgshlvealylvcgergffytpktrreaedlqvgqvelgggpgagslqplalegslqkrgiveqcctsicslyqlenycn"

# Slice from amino acid 1 to 24, i.e. from the beginning (index 0) up to, but not including, index 24
amino_acids_1_to_24 = full_amino_acid_sequence[0:24]

# Output
print(amino_acids_1_to_24)

# Count
print(len(amino_acids_1_to_24))

# Slice from amino acid 25 to 54, i.e. from index 24 up to, but not including, index 54
amino_acids_25_to_54 = full_amino_acid_sequence[24:54]

# Output
print(amino_acids_25_to_54)

# Count
print(len(amino_acids_25_to_54))

# Slice from amino acid 55 to 89, i.e. from index 54 up to, but not including, index 89
amino_acids_55_to_89 = full_amino_acid_sequence[54:89]

# Output
print(amino_acids_55_to_89)

# Count
print(len(amino_acids_55_to_89))

# Slice from amino acid 90 to 110, i.e. from index 89 up to, but not including, index 110
amino_acids_89_to_110 = full_amino_acid_sequence[89:110]

# Output
print(amino_acids_89_to_110)

# Count
print(len(amino_acids_89_to_110))