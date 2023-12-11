import pandas as pd
import os

in_file = 'haspeede2_dev/haspeede2_dev_taskAB.tsv'
out_dir = './input_profilingUD'

def preprocessing(input_path):
    os.makedirs(out_dir)
    with open (in_file, 'r') as infile:
        lines = infile.readlines()
        for line in lines[1:]:
            row = line.strip().split('\t')
            ident = row[0]
            testo = row[1]
            hs = row[2]
            stereotype = row[3]
            out_file_title = f"{ident},{hs},{stereotype}"
            out_file = open( f"{out_dir}/{out_file_title}.txt", "w")
            out_file.write(f"{testo}")
preprocessing(in_file)

