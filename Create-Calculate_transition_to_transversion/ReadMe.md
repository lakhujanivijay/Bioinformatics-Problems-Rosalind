
#### The problem below is taken from [![Rosalind](http://rosalind.info/static/img/logo.png?v=1526042457 "Rosalind")](http://rosalind.info/problems/list-view/)

### Transition versus Transversion mutations

DNA substitution mutations are of two types. *Transitions* are interchanges of two-ring purines (`A G`) or of one-ring pyrimidines (`C T`): they therefore involve bases of similar shape. *Transversions* are interchanges of purine for pyrimidine bases, which therefore involve exchange of one-ring and two-ring structures.

Although there are twice as many possible transversions, because of the molecular mechanisms by which they are generated, transition mutations are generated at higher frequency  than transversions. As well, transitions are less likely to result in amino acid substitutions (due to "wobble"), and are therefore more likely to persist as "silent substitutions" in populations as single nucleotide polymorphisms (SNPs).
    
### Problem Definition

For DNA strings `s1` and `s2` having the same length, their transition/transversion ratio `R(s1,s2)` is the ratio of the total number of transitions to the total number of transversions, where symbol substitutions are inferred from mismatched corresponding symbols as when calculating Hamming distance.

Given: Two DNA strings `s1` and `s2` of equal length (at most `1 kbp`).

Return: The transition/transversion ratio `R(s1,s2)`

Sample Dataset
```
>Rosalind_0209
GCAACGCACAACGAAAACCCTTAGGGACTGGATTATTTCGTGATCGTTGTAGTTATTGGA
AGTACGGGCATCAACCCAGTT

>Rosalind_2200
TTATCTGACAAAGAAAGCCGTCAACGGCTGGATAATTTCGCGATCGTGCTGGTTACTGGC
GGTACGAGTGTTCCTTTGGGT
```
Sample Output
```
1.21428571429
```
