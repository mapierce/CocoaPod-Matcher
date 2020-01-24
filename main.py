#!/usr/bin/env python

import os
from sys import argv

def check_directory_is_valid():
	script_path = os.path.dirname(os.path.abspath( __file__ ))
	return os.path.isfile(script_path+"/Podfile") and os.path.isfile(script_path+"/Podfile.lock")

def read_arguments(args):
	if len(args) == 2:
		print "The parameter is " + argv[1]
	else:
		print "Please enter exactly one parameter"		

def main():
	# read_arguments(argv)
	print(check_directory_is_valid())

	
if __name__ == "__main__":
	main()