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
        
