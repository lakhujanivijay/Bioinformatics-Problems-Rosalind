### About the program

This program could be used to locate the start and stop coordinates of gaps (N's) in the fasta format sequences.

### Input 

Fasta format sequence file

```
>head_1
AGGTANNGATCG
>head_2
GGGTTNNGGTTNNN
>head_3
```

### Output

Coordinates of gaps in `BED` format

```
head_1	5	7
head_2	5	7
head_2	11	14
head_3	0	2
```

### Usage

`python locate_gaps.py -i fasta_file.fa`
