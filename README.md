# Bioinformatics-Scripts
from Bio import SeqIO

records=[]
records_dict={}

for seq_record in SeqIO.parse("fasta.fasta", "fasta"):
    records_dict[str(seq_record.seq)]=seq_record.id
    records.append(str(seq_record.seq))


for i in range(0, len(records)):
    for k in range(0, len(records)):
        if i!=k:
            if records[i][-3:]==records[k][:3]:
                print records_dict[records[i]],records_dict[records[k]]
                   
