# Bioinformatics-Scripts

A short overlap graph - overlap graphs are used in denovo assembly
http://bioinformatics.oxfordjournals.org/content/early/2014/06/19/bioinformatics.btu395

Problem

A graph whose nodes have all been labeled can be represented by an adjacency list, in which each row of the list contains the two node labels corresponding to a unique edge.

A directed graph (or digraph) is a graph containing directed edges, each of which has an orientation. That is, a directed edge is represented by an arrow instead of a line segment; the starting and ending nodes of an edge form its tail and head, respectively. The directed edge with tail vv and head ww is represented by (v,w)(v,w) (but not by (w,v)(w,v)). A directed loop is a directed edge of the form (v,v)(v,v).

For a collection of strings and a positive integer kk, the overlap graph for the strings is a directed graph OkOk in which each string is represented by a node, and string ss is connected to string tt with a directed edge when there is a length kk suffix of ss that matches a length kk prefix of tt, as long as s≠ts≠t; we demand s≠ts≠t to prevent directed loops in the overlap graph (although directed cycles may be present).

Given: A collection of DNA strings in FASTA format having total length at most 10 kbp.

Return: The adjacency list corresponding to O3O3. You may return edges in any order.

				Solution:
				I have used Biopython parser to parse multifasta. The logic is quite simple, take a sequence, take it's suffix (3 mer) and compare it with prefix(3 mer) of another sequence (Checkpoint -This pair to check should be different). Then, if found a match, fetch the IDs. Voila!!
