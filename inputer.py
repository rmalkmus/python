#!/bin/python
import subprocess 
line_array = []
while True:
    question = raw_input("type what you'd like to add ")
    if question != "":
        line_array.append("%s\n" % question) 
    else:
        break        

with open("/var/tmp/inputer.txt", "w") as file:
    file.writelines(line_array)
#var_input = raw_input("insert line that you'd like to append to file ")
#code = subprocess.call(["cat", "/var/tmp/inputer.txt"])
#print(code)
#print(file.read())
