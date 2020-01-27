#!/usr/bin/env python

import os
import constants
from sys import argv

def check_directory_is_valid():
	script_path = os.path.dirname(os.path.abspath( __file__ ))
	return os.path.isfile(script_path+constants.PODFILE) and os.path.isfile(script_path+constants.PODFILE_LOCK)

def read_podfile_lock():
	podfile_lock = open(os.path.dirname(os.path.abspath( __file__ ))+constants.PODFILE_LOCK, "r")
	lines = podfile_lock.readlines()
	dependencies_index = lines.index(constants.DEPENDENCIES_STRING)
	valid_pods = list(filter(lambda x: x.startswith(constants.INSTALLED_POD_PREFIX), lines[0:dependencies_index])) 
	pods = dict(map(lambda x: split_text_to_pod_and_version(x), valid_pods))
	podfile_lock.close()
	return pods

def read_podfile():
	podfile = open(os.path.dirname(os.path.abspath(__file__))+constants.PODFILE, "r")
	podfile_stripped = list(map(lambda x: x.strip(), podfile.readlines()))
	valid_pods = list(filter(lambda x: x.startswith("pod "), podfile_stripped))
	unversioned_pod_text = list(filter(lambda x: "," not in x, valid_pods))
	unversioned_pods = list(map(lambda x: x[x.index("'")+1:-1], unversioned_pod_text))
	podfile.close()
	return unversioned_pods

def update_podfile(versioned_pods, unversioned_pods):
	podfile = open(os.path.dirname(os.path.abspath(__file__))+constants.PODFILE, "r")
	for key, val in versioned_pods.items():
		print(key, val)

def split_text_to_pod_and_version(text):
	items = text.split(constants.OPEN_BRACKET)
	pod_name = items[0].strip()[2:]
	pod_version = items[1].strip().split(constants.CLOSE_BRACKET)[0]
	return pod_name, pod_version

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
		versioned_pods = read_podfile_lock()
		unversioned_pods = read_podfile()
		update_podfile(versioned_pods, unversioned_pods)
	# read_arguments(argv)