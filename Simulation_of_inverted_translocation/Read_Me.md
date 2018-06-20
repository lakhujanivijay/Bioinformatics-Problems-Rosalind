#### Simlation of inverted translocation

This program simulates addition of reverse complementary sub sequence to a desired location simulating inverted translocation
and then generating random reads out of the new sequence.


#### Problem Definition

Let `S` is the sequence corresponding to a reference genome. If the segement of `S` from the i <sup>th</sup> 
  base to the jth base are deleted, inverted (i.e. reverse-complemented), and inserted after the kth 
  base, output the modified genomic sequences, `S'`. 

Also, generate 100 reads of length 150 from the modified sequence `S'` starting at random locations.
