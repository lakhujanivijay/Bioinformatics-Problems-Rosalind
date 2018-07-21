This script takes a fastq file and gives a text file as output where each line has the read numbr followed by a character string "`-`" followed by the average phred score for that read. See below example:

```
Read:36------------------------------------36

Read:40---------------------------------------39

Read:44-----------------------------------35

Read:48--------------------------------------38

Read:52--------------------------26

Read:56------------------------------------36

Read:60----------------------------------34
```

This helps in assessing the average quality score for each read visually.
The length of character string `-----` (hyphens) represents the average qual score i.e if read quality is `36`, the string will have `36` `-` (hyphen) characters.

### About the scripts

- `plot.py` : uses Biopython package for reading fastq and fetching qualities.
- `plot_without_biopython_dependency.plot` : This is the same implementation but without using Biopython package.
