
### What is Hamming distance ?

By definition from Wikipedia, the Hamming distance between two strings of equal length is the number of positions at which the corresponding symbols are different. In other words, it is the number of substitutions required to transform one string into another. Given two strings of equal length, this script computes the Hamming distance.

### Problem definition

We say that position `i` in k-mers `p1 … pk and q1 … qk` is a mismatch if `pi ≠ qi`. For example, `CGAAT` and `CGGAC` have two mismatches. The number of mismatches between strings `p` and `q` is called the Hamming distance between these strings and is denoted HammingDistance`(p, q)`.

#### Hamming Distance Problem

Compute the Hamming distance between two DNA strings.

Given: Two DNA strings.

Return: An integer value representing the Hamming distance.
Sample Dataset

```
GGGCCGTTGGT
GGACCGTTGAC
```
Sample Output
```
3
```
