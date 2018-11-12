#!/usr/bin/python
"""
Python 3.6
External Unix shell command can be wrapped in python code. 
Usage : python python_wrapper_for_shell_command.py <shell command>
	Eg: python python_wrapper_for_shell_command.py "dir"
		python python_wrapper_for_shell_command.py "ls"
"""

import subprocess
import sys

def command():
	cmd= sys.argv[1]
	status, output  = subprocess.getstatusoutput(cmd)
	if status != 0:
		print ("Command Execution Failed")
	return output.strip()

print ("\n********** Start:   ************")	
print ("\nStart python_wrapper_for_shell_command Execution !!!!\n")

if len(sys.argv) != 2:
	print ("Number of arguments not equal to 2. Exiting ...")
	exit()

x = command()
print ("Output: \n%s" %(x))
print ("\n********** End:   ************\n")
