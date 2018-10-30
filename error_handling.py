#!/bin/python
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("file_name", help="specify a file")
parser.add_argument("line_number", type=int, help="specify line number")
args = parser.parse_args()

try:
    with open(args.file_name) as f:
        read_file = f.readlines() #The readlines() function makes an array
        line = read_file[args.line_number -1]
except IndexError:
    print("Error: file '%s' doesn't have %i lines." % (args.file_name, args.line_number))
except IOError:
    print("There was an IOError.  '%s' does not exist" % args.file_name)
else:
    print(line)
