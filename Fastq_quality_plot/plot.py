#!/usr/bin/python3
__author__ = "Vijay Lakhujani"
__credits__ = ["Vijay Lakhujani"]
__version__ = "1.0"
__email__ = "lakhjanivijay@gmail.com"
__status__ = "done"


from Bio import SeqIO
import getopt, sys, re

def usage():
    print "Usage: plot.py -i <input_fastq> -o <plot.txt>"
    
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

line_number,rec=0,0
plot=[]

print "started..."


for record in SeqIO.parse(input_file, "fastq"):
    rec+=1
    score=record.letter_annotations["phred_quality"]
    mean_score=sum(score)/len(score)
    if rec%100000==0:
            print " plotted till ..." + str(rec)
    for i in range(0,mean_score):
        plot.append("-")
    out.write("Read:"+str(rec)+str(''.join(plot))+""+str(mean_score)+"\n")
    plot=[]
    score=0
    mean_score=0

out.close()
print "\ncompleted...!"
