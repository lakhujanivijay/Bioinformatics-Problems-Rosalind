import re
file= open('50_S1_L001_R1_001.fastq')
fasta = open('result_fasta.fasta', 'w')
seq_count=0
for line in file:
    sequence=re.search('[ATCG]+\n', line)  
    if sequence:
        seq_count+=1
        fasta.write('>'+'seq_'+ str(seq_count)+'\n')
        fasta.write(sequence.group())
        
fasta.close()       
