#!/usr/bin/env python

import os
import constants

def check_directory_is_valid():
	script_path = os.path.dirname(os.path.abspath( __file__ ))
	return os.path.isfile(script_path+constants.PODFILE) and os.path.isfile(script_path+constants.PODFILE_LOCK)

def read_podfile_lock():
	print("Reading Pod versions from lock file...")
	podfile_lock = open(os.path.dirname(os.path.abspath( __file__ ))+constants.PODFILE_LOCK, "r")
	lines = podfile_lock.readlines()
	dependencies_index = lines.index(constants.DEPENDENCIES_STRING)
	valid_pods = list(filter(lambda x: x.startswith(constants.INSTALLED_POD_PREFIX), lines[0:dependencies_index])) 
	pods = dict(map(lambda x: split_text_to_pod_and_version(x), valid_pods))
	podfile_lock.close()
	return pods

def update_podfile(versioned_pods):
	print("Updating Pod versions...")
	podfile = open(os.path.dirname(os.path.abspath(__file__))+constants.PODFILE, "r")
	updated_podfile = open(os.path.dirname(os.path.abspath(__file__))+constants.PODFILE_TMP, "w")
	for line in podfile.readlines():
		stripped_line = line.strip()
		if stripped_line.startswith(constants.POD_PREFIX) and ", " not in stripped_line:
			unversioned_pod = stripped_line[stripped_line.index("'")+1:-1]
			updated_line = line.rstrip(constants.NEW_LINE) + ", '" + versioned_pods[unversioned_pod] + "'" + constants.NEW_LINE
			updated_podfile.write(updated_line)
		else :
			updated_podfile.write(line)

def overwrite_podfile():
	print("Writing to Podfile...")
	os.rename(os.path.dirname(os.path.abspath(__file__))+constants.PODFILE_TMP, os.path.dirname(os.path.abspath(__file__))+constants.PODFILE)

def split_text_to_pod_and_version(text):
	items = text.split(constants.OPEN_BRACKET)
	pod_name = items[0].strip()[2:]
	pod_version = items[1].strip().split(constants.CLOSE_BRACKET)[0]
	return pod_name, pod_version

if __name__ == "__main__":
	if check_directory_is_valid() is False:
		print("A Podfile and/or a Podfile.lock were not found in the current directory")
	else:
		print("Valid files found")
		update_podfile(read_podfile_lock())
		overwrite_podfile()
		print("Done")








