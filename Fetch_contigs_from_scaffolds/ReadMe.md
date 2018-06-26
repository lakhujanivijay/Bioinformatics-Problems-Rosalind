

A _**scaffold**_ is a portion of the genome sequence reconstructed from end-sequenced whole-genome shotgun clones.
Scaffolds are composed of contigs and gaps. 

A _**contig**_ is a contiguous length of genomic sequence in which the order of bases is known to a high confidence level.
Gaps occur where reads from the two sequenced ends of at least one fragment overlap with other reads in two different contigs (as long as the arrangement is otherwise consistent with the contigs being adjacent). Since the lengths of the fragments are roughly known, the number of bases between contigs can be estimated.

> Courtesy: [Joint Gneome Institute](https://genome.jgi.doe.gov/portal/help/scaffolds.jsf)

### About the script:

The script reads a scaffold file (could be from CLC genomics workbench or any assembler) and generates a contig file by splitting the sequences by `n` or `N`.

#### Input:

```
>scaffold1
ACTGTGCATNNNNNNACGCTGCANnnNNCTGCAnnnCTGCAnnNNNNCTGCA
>scaffold2
ACGACGACGCGATAGAGnnnnnnAGACGAGAGNNNnnACGACGACG
```

#### Output:

```
>contig_1
ACGCTGCA
>contig_2
CTGCA
>contig_3
CTGCA
>contig_4
CTGCAACGACGACGCGATAGAG
>contig_5
AGACGAGAG
>contig_6
ACGACGACG
```
