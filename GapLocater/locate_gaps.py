from Bio import SeqIO
import re, getopt, sys

def usage():
    print "Usage: locate_gaps.py -i <input_fasta.fa>"

try:
    options, remainder=getopt.getopt(sys.argv[1:], 'i:h')

except getopt.GetoptError as err:
    print str(err)
    usage()
    sys.exit()

for opt, arg in options:
    if opt in ('-i'):
        input_file=arg
    if opt in ('-h'):
        usage()
	sys.exit()

try:
    file = open(input_file)
 
except IOError:
    print "fasta file cannot be opened"

p = re.compile(r'N+')

for record in SeqIO.parse(file, "fasta"):
    seq=str(record.seq)
    for m in p.finditer(seq): 
        if m:
            print str(record.id) + "\t" + str(m.start()) + "\t"+ str(m.end())


       
