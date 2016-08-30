#!/usr/bin/python3
__author__="Vijay Lakhujani"
__date__="23/07/2016"
__email__="lakhujanivijay@gmail.com"
__status__ = "done"

import urllib2, re
ids=open("ids.txt")
for acc in ids:
    acc=acc.rstrip()
    pos=[]
    link = "http://www.uniprot.org/uniprot/"+acc+".fasta"
    data = urllib2.urlopen(link)
    seq = ''.join([line.rstrip('\n') for line in data if not (line.startswith('>'))])
    p = re.compile(r'(?=(N[^P][S/T][^P]))')
    for m in p.finditer(seq): 
        pos.append(m.start() + 1)
    if len(pos)!=0:        
        print acc
        print(" ".join(str(x) for x in pos))
