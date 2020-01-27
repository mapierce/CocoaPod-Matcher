#!/usr/bin/env python

import os
import constants
from sys import argv

def check_directory_is_valid():
	script_path = os.path.dirname(os.path.abspath( __file__ ))
	return os.path.isfile(script_path+constants.PODFILE) and os.path.isfile(script_path+constants.PODFILE_LOCK)

def read_podfile_lock():
	podfile_lock = open(os.path.dirname(os.path.abspath( __file__ ))+constants.PODFILE_LOCK, "r").readlines()
	dependencies_index = podfile_lock.index(constants.DEPENDENCIES_STRING)
	valid_pods = list(filter(lambda x: x.startswith(constants.INSTALLED_POD_PREFIX), podfile_lock[0:dependencies_index])) 
	pods = dict(map(lambda x: split_text_to_pod_and_version(x), valid_pods))
	for key, val in pods.items():
		print(key, val)

def split_text_to_pod_and_version(text):
	items = text.split("(")
	pod_name = items[0].strip()[2:]
	pod_version = items[1].strip().split(")")[0]
	return pod_name, pod_version
	# print(pod_name + ": " + pod_version)

def read_arguments(args):
	if len(args) == 2:
		print "The parameter is " + argv[1]
	else:
		print "Please enter exactly one parameter"		

	
if __name__ == "__main__":
	if check_directory_is_valid() is False:
		print("A Podfile and a Podfile.lock were not found in the current directory")
	else:
		print("Valid files found")
		read_podfile_lock()
	# read_arguments(argv)