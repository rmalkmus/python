#!/bin/python

#python -m SimpleHTTPServer 5500


import subprocess
import os
import argparse
import sys

parser = argparse.ArgumentParser(description="kill the running process listening on a given port")
parser.add_argument("port", help="give port number", type=int)

args = parser.parse_args()




def check_n_kill(port_number):
    #check to see if port_number is currently in use
    try:
        exit_code_status = subprocess.call(["lsof", "-n", "-i4TCP:%s" % port_number])
        check_port = subprocess.check_output(["lsof", "-n", "-i4TCP:%s" % port_number])
        if exit_code_status == 0:
            pid_array = check_port.split()
            pid = pid_array[10]
            print("We have detected port %s as 'in use', we are going to kill it." % port_number)
            os.kill(int(pid), 9)
    except subprocess.CalledProcessError:
        print("looks like that port %s is open, you are clear to proceed" % port_number)
        sys.exit(99)

check_n_kill(args.port)


if sys.exit == 99:
    print("booga booga booga!!!")
    
