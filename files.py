#!/bin/python 

file = open('awk.txt', 'a')


file.write("happy1\n")

for i in file:
    print (i)

file.close()
