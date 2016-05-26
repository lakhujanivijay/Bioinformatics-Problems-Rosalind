#!/usr/bin/python3
__author__ = "Vijay Lakhujani"
__credits__ = ["Vijay Lakhujani"]
__version__ = "1.0"
__email__ = "lakhjanivijay@gmail.com"
__status__ = "done"

file = open('stats.txt')

lengths=[]
sums=0

for line in file:
    line=line.rsplit()
    if line[0]!="ID":
        lengths.append(int(line[1]))
        lengths=sorted(lengths, reverse=True)

print lengths
N_half=sum(lengths)/2

for i in range(0, len(lengths)):
    sums=sums+lengths[i]
    if sums >= N_half:
        print "N_50:",lengths[i-1]
        break
        
