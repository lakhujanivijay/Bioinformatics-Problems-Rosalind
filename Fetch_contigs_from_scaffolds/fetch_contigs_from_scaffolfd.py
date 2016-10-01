#!/usr/bin/python3
__author__ = "Vijay Lakhujani"
__credits__ = ["Vijay Lakhujani"]
__version__ = "1.0"
__email__ = "lakhujanivijay@gmail.com"
__status__ = "done"

#!/usr/bin/python2.7

from Bio import SeqIO
import getopt,sys,re


def usage():
    print "Usage: contig_from_scaffold.py -i <input_scaffold_fasta> -o <output_contig_fasta>"

try:
    options, remainder=getopt.getopt(sys.argv[1:], 'i:o:h')

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
    elif opt in ('-o'):
        output_file=arg

out=open(output_file, 'w')

sequence = ''.join([str(record.seq).strip() for record in SeqIO.parse(input_file, "fasta")])

m=re.sub('[nN]+','\n',sequence).split('\n')

for i in range(1,len(m)):
    out.write('>contig_'+str(i)+'\n')
    out.write(m[i]+'\n')
