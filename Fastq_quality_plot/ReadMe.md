### About the scripts

These scripts reads the phred score string from fastQ file (offset should be 33) and gives a text file as output. 
The output file looks something like this:
```    
    Read:1--------------------20
    Read:2----------------------22
    Read:3-----------------------23
    Read:4----------------------22
    Read:5----------------------22
    Read:6------------------------24
    Read:7-----------------------------29
    Read:8----------------------------28
    Read:9-------------------------25
    Read:10---------------------------27
    Read:11----------------------------28
    Read:12-----------------------------29
    Read:13-----------------------------29
  ```  
   
Here each line has the read number followed by a string having "`-`" character whose length corresponds to the average read quality followed by the average phred score.
    
### How does it works?
    
1. script reads the fastq file.
2. fetch the phred score (base call quality for each base).
3. calculates the average quality for each read.
4. prints a string having hyphen character ("`-`") for each read whose length corresponds to the average quality of that read.

say for `read#10`, the average phred score is `27`, the output will be like:

`Read:10---------------------------27` (Notice, there are `27` "`-`") characters.

###  Running the script:
`> python plot.py -i test.fastq -o plot.txt`
    
### Usage 
`> python plot.py -h`

### About the scripts

- [`plot.py`](https://github.com/lakhujanivijay/Bioinformatics-Scripts/blob/master/Fastq_quality_plot/plot.py) : uses Biopython package for reading fastq and fetching qualities.

- [`plot_without_biopython_dependency.plot`](https://github.com/lakhujanivijay/Bioinformatics-Scripts/blob/master/Fastq_quality_plot/plot_without_biopython_dependency.plot): This is the same implementation but without using Biopython package.
