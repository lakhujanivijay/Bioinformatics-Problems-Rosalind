### What is N50 ?

Contig or scaffold `N50` is a weighted median statistic such that `50%` of the entire assembly is contained in contigs or scaffolds equal to or larger than this value.

### Mathematically

Given a set of sequences of varying lengths, the `N50` length is defined as the length `N` for which `50%` of all bases in the sequences are in a sequence of length `L < N`. This can be found mathematically as follows: Take a list L of positive integers. Create another list `L'` , which is identical to `L`, except that every element `n` in `L` has been replaced with `n` copies of itself. Then the median of `L'` is the `N50` of `L`. For example: If `L = {2, 2, 2, 3, 3, 4, 8, 8}`, then `L'` consists of six `2's`, six `3's`, four `4's`, and sixteen `8's`; the `N50` of `L` is the median of `L'` , which is `6`.

### In simple words

scaffold `N50` is the median contig size of your genomic assembly. It's a metric that you can use to evaluate the quality of your assembly, since an overly small `N50` suggests that you were unable to generate many contigs of biologically meaningful size (i.e. you probably have a lot of bogus little contigs in your assembly). You can increase your `N50` by eliminating sequences which are bound to cause you problems, e.g. short repetitive stretches.

Note that this metric only applies when doing de novo assembly. If you are aligning to a reference (i.e. for variant discovery applications) this metric doesn't apply

> Source: [StackExchange](http://biology.stackexchange.com/questions/34122/an-example-for-n50-why-do-we-need-it)

### About this script

`N50.py` : This script takes the `stats.txt` file (coming out from [velvet](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2952100/) denovo assembler) as input and calculates `N50` value.

`calc_n50_from_assembly_fasta.py` : This script takes a multifasta file (assembly file having scaffolds) and calculate `N50` value.

