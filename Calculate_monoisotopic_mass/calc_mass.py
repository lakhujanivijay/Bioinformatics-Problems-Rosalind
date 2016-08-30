
#!/usr/bin/python3
__author__ = "Vijay Lakhujani"
__credits__ = ["Vijay Lakhujani"]
__version__ = "1.0"
__email__ = "lakhujanivijay@gmail.com"
__status__ = "done"

import re 

mass=open("mass.txt")

monoisotopic_mass=[]

weight_table={}

for amino_acid in mass:
    amino_acid=(re.split(r'\s', amino_acid.rstrip()))
    weight_table[amino_acid[0]]= amino_acid[1]

sequence=open("protein.txt")

for line in sequence:
    for i in range(0, len(list(line.rstrip()))):
        monoisotopic_mass.append(float(weight_table[(line.rstrip())[i]]))


print round(sum(monoisotopic_mass),3)
