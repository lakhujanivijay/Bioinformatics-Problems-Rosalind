This script takes a fastq file and gives a text file as output where each line has the read numbr followed by a character string "_ _ _ " followed by the average phred score for that read. See below example
:

Read:36------------------------------------36

Read:40---------------------------------------39

Read:44-----------------------------------35

Read:48--------------------------------------38

Read:52--------------------------26

Read:56------------------------------------36

Read:60----------------------------------34

This helps in assesing the average quality score for each read visually.
The length of character string _ _ _ _(dashes)represents the average qual score i.e if read quality is 36, the string will have 36 _ (dash) characters.
