#!/usr/bin/env python
#-*- coding:utf-8 -*-
################################################
# File Name: getSequenceReads.py
# Author: Mischa Lundberg
# Mail: mischa.lundberg@regionh.dk
################################################

__version__ = '0.1.0'
import sys
import os
import argparse
import time

infile="test.fa"
outfilename=""
read_starter=">"
get_n_reads=2
start_on_read=2

def main():
    parser = argparse.ArgumentParser(description = "Code to run ourGWAS with VCF, Plink1/2, and tsv files")
    parser.add_argument('--input', 
        type = str, 
        help = "Path to input file; please supply filename as following \"dir/to/input_file.fa\"", 
        required = True)
    parser.add_argument('--readIdentifier', 
        type = str, 
        help = "Identifier of each read, i.e. > or #; use quotes. Default: \">\"", 
        required = False,
        default = ">")
    parser.add_argument('--nReads', 
        type = int, 
        help = "How many reads you want to output", 
        required = True)
    parser.add_argument('--firstRead', 
        type = int, 
        help = "At which read the ourput should start. Default: 1 {first read)", 
        required = False,
        default=1)
    parser.add_argument('--output', 
        type = str, 
        help = "Path to output file; please supply filename as following \"dir/to/input_file.fa\"", 
        required = True)
    
    args = parser.parse_args()
    
    parsed_data = parse_sequences(args.input, args.readIdentifier, args.nReads, args.firstRead)

    with open(args.output, 'w') as f:
        for line in parsed_data:
            f.write(line)
    print("Output file saved here: ",args.output)



   

    

def parse_sequences(infile,read_starter,get_n_reads,start_on_read):
    output=[]
    with open(infile) as f:
        count=0
        seqs = f.readlines()
        i=0
        flen=len(seqs)
        run=True
        if start_on_read == 0:
            get_n_reads+=1
        while run: 
            seq=seqs[i]   
            #print(count) 
            #check for next iteration
            if count-start_on_read+1 >= get_n_reads or i+1 >= flen:
                run=False
            #
            if seq.startswith(read_starter):
                count += 1
                #print(count,"in if")
                if count >= start_on_read:
                    #print("in if in if")
                    output.append(seq)
            else:
                #print("in else")
                if count >= start_on_read:
                    #print("in if in else")
                    output.append(seq)
            i+=1
    return(output)

parse_sequences(infile,">",3,0)
