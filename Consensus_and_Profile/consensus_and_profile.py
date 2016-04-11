
fasta= open("fasta.txt")
seq=[]
all_seq={}

for line in fasta:
    line=line.rstrip()
    if not line.startswith(">"):
        seq.append(line)
        
    else:
        print line,seq
        all_seq[line]= seq
        seq=[]


seq_list,base,a,c,g,t=[],[],[],[],[],[]


seq_list.append(list(line))




for j in range(len(seq_list[0])):
    base=[]
    for i in range(len(seq_list)):
        base.append(seq_list[i][j])

    a.append(base.count('A'))
    c.append(base.count('C'))
    g.append(base.count('G'))
    t.append(base.count('T'))
    
print "A:", ' '.join(str(x) for x in a)
print "C:", ' '.join(str(x) for x in c)
print "G:",' '.join(str(x) for x in g)
print "T:",' '.join(str(x) for x in t)
