To allow for the presence of its varying forms, a protein motif is represented by a shorthand as follows: `[XY]` means "either `X` or `Y`" and `{X}` means "any amino acid except `X`." For example, the N-glycosylation motif is written as `N{P}[ST]{P}`.

This scripts takes as input, a text file having UniProt protein accessions and fetches the corresponding amino acid sequence and then tried to
find the N-glycosylation motif is written as `N{P}[ST]{P}`.

**Given**: At most `15` UniProt Protein Database access IDs.

**Return**: For each protein possessing the N-glycosylation motif, output its given access ID followed by a list of locations in the protein string where the motif can be found.


**Sample Dataset**
```
A2Z669
B5ZC00
P07204_TRBM_HUMAN
P20840_SAG1_YEAST
```
**Sample Output**
```
B5ZC00
85 118 142 306 395
P07204_TRBM_HUMAN
47 115 116 382 409
P20840_SAG1_YEAST
79 109 135 248 306 348 364 402 485 501 614
```
