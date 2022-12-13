#!/usr/bin/env python
#-*- coding:utf-8 -*-
################################################
# File Name: ExSeq.py
# Author: Mischa Lundberg
# Mail: mischa.lundberg@regionh.dk
################################################

__version__ = '0.1.1'
import sys
import os
import argparse
import time
from itertools import chain

def main(args):
    parsed_data = parse_sequences(args.input, args.readIdentifier, args.nReads, args.firstRead, args.excludeReads)

    with open(args.output, 'w') as f:
        for line in parsed_data:
            f.write(line)
    print("Output file saved here: ",args.output)

    

def parse_sequences(infile,read_starter,get_n_reads,start_on_read,seq_exclusions):
    output=[]
    exclusions=False
    to_exclude = []
    if seq_exclusions != "":
        if os.path.isfile(seq_exclusions):
            with open(seq_exclusions) as exc_file:
                to_exclude = exc_file.readlines()
            exclusions=True
        elif isinstance(seq_exclusions, str):
            to_exclude = seq_exclusions.split(",")
            exclusions=True
        else:
            print("Could not identify your input of sequences to exclude. Exiting!")
            sys.exit()
        cleaned_exc = []
        for i in to_exclude:
            cleaned_exc.append(i.replace("\n", ""))
        to_exclude = cleaned_exc
    print(to_exclude)
    with open(infile) as f:
        count=0
        seqs = f.readlines()
        i=0
        flen=len(seqs)
        run=True
        exclude_current_sequence=False

        if exclusions:
            tmp = []
            for curr_exc in to_exclude:
                tmp.append(list(filter(lambda i: curr_exc[0] in i, seqs))[0])
            print("Excluding up to ",len(to_exclude)," sequences")
        if start_on_read == 0:
            get_n_reads+=1
        while run: 
            seq=seqs[i]
            #check for next iteration
            if count-start_on_read+1 >= get_n_reads or i+1 >= flen:
                run=False
            if seq.startswith(read_starter):
                count += 1
                if exclusions:
                    if seq.replace("\n", "") in to_exclude: #any(seq in i for i in to_exclude):
                        exclude_current_sequence = True
                        count-=1
                    else:
                        exclude_current_sequence = False
                if count >= start_on_read and not(exclude_current_sequence):
                    output.append(seq)
            else:
                if count >= start_on_read and not(exclude_current_sequence):
                    output.append(seq)
            i+=1
    return(output)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description = "Method to extract a selected number of sequences from a sequencing file, e.g., Bisulfite/Fasta")
    parser.add_argument('-i','--input', 
        type = str, 
        help = "Path to input file; please supply filename as following \"dir/to/input_file.fa\"", 
        required = True)
    parser.add_argument('-r','--readIdentifier', 
        type = str, 
        help = "Identifier of each read, i.e. > or #; use quotes. Default: \">\"", 
        required = False,
        default = ">")
    parser.add_argument('-n','--nReads', 
        type = int, 
        help = "How many reads you want to output", 
        required = True)
    parser.add_argument('-f','--firstRead', 
        type = int, 
        help = "At which read the ourput should start. Default: 1 {first read)", 
        required = False,
        default=1)
    parser.add_argument('-e','--excludeReads', 
        type = str, 
        help = "A file with sequences to exclude from the output. Alternatively, it also can be a comma separated list.", 
        required = False,
        default="")
    parser.add_argument('-o','--output', 
        type = str, 
        help = "Path to output file; please supply filename as following \"dir/to/input_file.fa\"", 
        required = True)
    
    args = parser.parse_args()
    
    main(args)
