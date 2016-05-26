### ReadMe ####

'''
    This simmple script takes a fasta file and gives out a tab separated text file with column1 having fasta ID
    and column 2 having sequence length
'''

#!/usr/bin/python2.7
__author__ = "Vijay Lakhujani"
__credits__ = ["Vijay Lakhujani"]
__version__ = "1.0"
__email__ = "lakhujanivijay@gmail.com"
__status__ = "done"

from Bio import SeqIO

seq_length_list=[]

try:
    file = open("test.fasta")
    out  = open("out.txt", 'w')
    
except IOError:
    print "file cannot be opened"

for record in SeqIO.parse(file, "fasta"):
    seq_length_list.append(len(record.seq))
    out.write(record.id + "\t" + str(len(record.seq)))
    out.write("\n")

out.close()
file.close()
