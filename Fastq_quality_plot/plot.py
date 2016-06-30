#!/usr/bin/python3
__author__ = "Vijay Lakhujani"
__credits__ = ["Vijay Lakhujani"]
__version__ = "1.0"
__email__ = "lakhjanivijay@gmail.com"
__status__ = "done"

''' 
    Running the script:
    > python plot.py -i test.fastq -o plot.txt
    
    For USAGE:
    > python plot.py -h

    This scripts reads the phred score string from fastQ file (offset should be 33) and gives a text file as output. 
    The output file looks something like this:
    
    Read:1--------------------20
    Read:2----------------------22
    Read:3-----------------------23
    Read:4----------------------22
    Read:5----------------------22
    Read:6------------------------24
    Read:7-----------------------------29
    Read:8----------------------------28
    Read:9-------------------------25
    Read:10---------------------------27
    Read:11----------------------------28
    Read:12-----------------------------29
    Read:13-----------------------------29
    
    Here each line has the read number followed by a string having "-" character
    whose length corresponds to the average read quality followed by the average phred score.
    
    HOW DOES IT WORKS?
    
    1. script reads the fastq file.
    2. fetch the phred score (base call quality for each base).
    3. calculates the average quality for each read.
    4. prints a string having hyphen character ("-") for each read whose length corresponds to the average quality of that read.
    
    say for read#10, the average phred score is 27, the output will be like:
    Read:10---------------------------27 (Notice, there are 27 "-") charachters.

'''


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
