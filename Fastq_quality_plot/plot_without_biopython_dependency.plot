#!/usr/bin/python3
__author__ = "Vijay Lakhujani"
__credits__ = ["Vijay Lakhujani"]
__version__ = "1.0"
__email__ = "lakhujanivijay@gmail.com"
__status__ = "done"

try:
    file =open("test.fq")
    out=open("out.txt", 'w')
    
except IOError:
    print("Error: File does not appear to exist.")

line_number=0
plot=[]

print "started..."
for line in file:
    line_number=line_number+1
    line=line.rstrip()
    if line_number%4==0:
        score=map(lambda x: ord(x)-33,list(str(line)))
        mean_score=sum(score)/len(score)
        for i in range(0,mean_score):
            plot.append("-")
        out.write("Read:"+str(line_number)+str(''.join(plot))+""+str(mean_score)+"\n")
    if line_number%100000==0:
        print "     plotting .."
    plot=[]
    score=0
    mean_score=0

out.close()
print "\ncompleted...!"
