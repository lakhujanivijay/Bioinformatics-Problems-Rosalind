from Bio import SeqIO
percent={}

for seq_record in SeqIO.parse("rosalind_gc.txt", "fasta"):
    gc_count = str(seq_record.seq).count('G') + str(seq_record.seq).count('C')
    percent[float(gc_count)/float(len(seq_record))*100.0] = seq_record.id

print percent[max(percent.keys())]
print max(percent.keys())
