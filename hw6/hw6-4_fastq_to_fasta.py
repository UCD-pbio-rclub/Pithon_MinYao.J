# Problem 4
# Write a function that converts a fastq file to a fasta file

import string
import re

print('Please enter fastqtofasta("input filename", "output filename")')

def fastqtofasta(input, output):
    fasta = open(input)
    fastq = open(output, 'w')
    count = 0
    for line in fasta:
        count += 1
        if count % 4 == 1:
            line = line[1:]  # get rid of the '@'
            fastq.write(">"+line)
        elif count % 4 == 2:
            fastq.write(line)
    fasta.close()
    fastq.close()
