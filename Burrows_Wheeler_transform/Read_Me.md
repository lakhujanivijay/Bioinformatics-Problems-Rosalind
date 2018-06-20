### What is Burrows Wheeler transform

The Burrows–Wheeler transform (BWT, also called block-sorting compression) rearranges a character string into runs
of similar characters. This is useful for compression, since it tends to be easy to compress a string that has runs 
of repeated characters by techniques such as move-to-front transform and run-length encoding. 
More importantly, the transformation is reversible, without needing to store any additional data. 

The BWT is thus a "free" method of improving the efficiency of text compression algorithms, costing only some extra computation.

### More information [here](http://tcs.rwth-aachen.de/lehre/Komprimierung/SS2012/ausarbeitungen/Burrows-Wheeler.pdf)

### About the script

This script takes a string and spits out burrows wheeler transformed string.
