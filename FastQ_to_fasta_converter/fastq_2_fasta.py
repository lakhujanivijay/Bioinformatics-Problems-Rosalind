
#!/usr/bin/python3
__author__ = "Vijay Lakhujani"
__credits__ = ["Vijay Lakhujani"]
__version__ = "1.0"
__email__ = "lakhujanivijay@gmail.com"
__status__ = "done"

import re
file= open('test.fastq')
fasta = open('test.fasta', 'w')
seq_count=0
for line in file:
    sequence=re.search('[ATCG]+\n', line)  
    if sequence:
        seq_count+=1
        fasta.write('>'+'seq_'+ str(seq_count)+'\n')
        fasta.write(sequence.group())
        
fasta.close()       
