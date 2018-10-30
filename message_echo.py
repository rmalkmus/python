#!/bin/python

echo = raw_input("what's your message? ")
count = raw_input("how many times? ")

if count:
    count = int(count)
else:
    count = 1

def message(message, count):
    i = 1
    while i <= count:
        print(message)
        i += 1

message(echo, count)
