
#!/usr/bin/python3
__author__ = "Vijay Lakhujani"
__credits__ = ["Vijay Lakhujani"]
__version__ = "1.0"
__email__ = "lakhjanivijay@gmail.com"
__status__ = "done"

from collections import Counter

file=open("seq.fa")

for line in file:
    counts = dict(Counter(list(line.rstrip())))

print counts['A'],counts['C'],counts['G'],counts['T']
