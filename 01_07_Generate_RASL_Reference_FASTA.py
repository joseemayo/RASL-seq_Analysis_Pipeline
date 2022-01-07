# 01/07/21 - José Mayorga
#
# This script is designed to generate the fasta alignment index for RASL-seq
# using the 40 bp probe sequences.
#
# The sequences are read in from a text file and the genes are separated by chromosome.
# The FA file is created by concatenating each sequence based on the order and on a
# per chromosome basis.

import pandas as pd

# Importing Sequence Data
probeSeq = pd.read_csv('Data_Files/01_07_V4_RASL_seq_Probe_Sequences.csv')

# Adding Chromosome label to each gene
probeSeq['chr'] = ''
for index in range(len(probeSeq['gene'])):
    probeSeq['chr'][index] = probeSeq['gene'][index][2] # 3rd position in the gene name is the chromosome number

# Opening output file
referenceFile = open('V4_RASL_Alignment_File.fa', 'w')

# Generating iteration series for chromosomes
chrOrder = ['1', '2', '3', '4', '5', 'C']

# Generating fasta sequence by appending all probe sequences together and writing to the fasta file
for chrIndex in chrOrder:
    referenceFile.write('>' + chrIndex + '\n') # Sequence header
    referenceFile.write((probeSeq[probeSeq['chr'] == chrIndex]['probe_sequence']).str.cat() + '\n') # Appended Sequence

# Closing the file
referenceFile.close()

#
