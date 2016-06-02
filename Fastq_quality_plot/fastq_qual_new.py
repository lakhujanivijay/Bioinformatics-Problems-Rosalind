from Bio import SeqIO

out=open("out.txt", 'w')

line_number,rec=0,0
plot=[]

print "started..."

for record in SeqIO.parse("test.fq", "fastq"):
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
