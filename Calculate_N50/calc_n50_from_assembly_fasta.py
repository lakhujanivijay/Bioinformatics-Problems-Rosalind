
#!/usr/bin/python3
__author__ = "Vijay Lakhujani"
__credits__ = ["Vijay Lakhujani"]
__version__ = "1.0"
__email__ = "lakhujanivijay@gmail.com"
__status__ = "done"


from Bio import SeqIO
import getopt, sys, re
lengths=[]
sums=0

def usage():
    print "Usage: N50.py -i <input_fasta>"
    print "Prints N50 in stdout"


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
    
for seq_record in SeqIO.parse(input_file, "fasta"):
    lengths.append(len(seq_record.seq))

lengths=sorted(lengths, reverse=True)

N_half=sum(lengths)/2

for i in range(0, len(lengths)):
    sums=sums+lengths[i]
    if sums >= N_half:
        print "N_50:",lengths[i]
        break
