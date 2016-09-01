# Overlap Graphs
# ==============
 
 A graph whose nodes have all been labeled can be represented by an adjacency

 list, in which each row of the list contains the two node labels corresponding
 to a unique edge.
 
 A directed graph (or digraph) is a graph containing directed edges, each of
 which has an orientation. That is, a directed edge is represented by an arrow
 instead of simply a segment; the starting and ending nodes of an edge form its
 tail and head, respectively. The directed edge with tail v and head w is
 represented by (v,w) (but not by (w,v)). A directed loop is a directed edge of
 the form (v,v).
 For a collection of strings and a positive integer k, the overlap graph for
 the strings is a directed graph Ok in which each string is represented by a
 node, and string s is connected to string t with a directed edge if and only
 if there is a length k suffix of s that matches a length k prefix of t.
 Directed loops are not allowed in the overlap graph.
 
 Given: A collection of DNA strings in FASTA format having total length at most
 10 kbp.
 
 Return: The adjacency list corresponding to O3.
 
 Sample Dataset
 --------------
 >Rosalind_0498
 AAATAAA
 >Rosalind_2391
 AAATTTT
 >Rosalind_2323
 TTTTCCC
 >Rosalind_0442
 AAATCCC
 >Rosalind_5013
 GGGTGGG
 
 Sample Output
 -------------
 Rosalind_0498 Rosalind_2391
 Rosalind_0498 Rosalind_0442
 Rosalind_2391 Rosalind_2323
