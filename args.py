#!/bin/python

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('filename', help='file to load')
parser.add_argument('--limit', '-l', type=int, help='the number of lines to read')
parser.add_argument('--version', '-v', action='version', version='%(prog)s 1.0')

args = parser.parse_args()

try:
    f = open(args.filename)
except IOError as err:
    print("Error: file not found")
else:
    with open (args.filename) as f:
        lines = f.readlines()
        lines.reverse()
        
        if args.limit:
            lines = lines[:args.limit]
    
        for i in lines:
            print(i.strip()[::-1])
finally:
    print("We've finished")

