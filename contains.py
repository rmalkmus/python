#!/bin/python

import argparse


parser = argparse.ArgumentParser(description="Pass this a snippit of what word you'd like to search for")
parser.add_argument("snippit", help="the string you'd like to search for")

args = parser.parse_args()
snippit = args.snippit.lower()
words = open("/usr/share/dict/words").readlines()
print([i.rstrip() for i in words if snippit in i.lower()])



