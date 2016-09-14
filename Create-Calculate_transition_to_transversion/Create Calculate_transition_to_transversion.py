from Bio import SeqIO

input_file=open("seq.fa")

purines=['A', 'G']
pyrimidines=['T', 'C']
sequences= []
transitions, transversions=0,0

for record in SeqIO.parse(input_file, "fasta"):
    sequences.append(list(record.seq))

for i in range(0,len(sequences[0])):
    for j in range(0,len(sequences[1])):
        if i==j and sequences[0][i] != sequences[1][j]:
               if sequences[0][i] in purines and sequences[1][j] in purines:
                   transitions+=1
               elif sequences[0][i] in pyrimidines and sequences[1][j] in pyrimidines:
                   transitions+=1
               else:
                   transversions+=1

print float(transitions)/float(transversions)

