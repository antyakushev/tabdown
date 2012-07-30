#!/usr/bin/env python
#
# t - A command line organization assistant for text files.
#
# ported to python on 07/28
# by Sean Lee

import subprocess
import sys
import os
from termcolor import colored

t_dir = "/home/slee2/t"
os.chdir(t_dir)

# Run with no parameters: List
if len(sys.argv)==1:
	# Sort alphabetically
	dirs = os.listdir(t_dir)
	dirs.sort()


	for dirname in dirs:
		if not dirname.startswith('.'):
			print(colored(dirname + ':', 'magenta'))
			print("\t"),

			dirpath=t_dir + "/" + dirname
			
			# Sort by last modified
			files = os.listdir(dirpath)
			files.sort(key=lambda x: os.path.getmtime(dirpath + "/" + x))
			files.reverse()
			
			functions=[]

			for file in files:
				filepath=dirpath + "/" + file
				if not file.startswith('.'):
					if os.access(filepath, os.X_OK):
						functions.append(file)
					else:
						print(file + ' '),
			for func in functions:
				print(colored(func, 'green') + "\t"),

			print('')
else:
	for dirname in os.listdir(t_dir):
		if not dirname.startswith('.'):
			dirpath=t_dir + "/" + dirname

			for file in os.listdir(dirpath):
				filepath = dirpath + '/' + file

				if sys.argv[1] == file:

					# Launch if executable
					if os.access(filepath, os.X_OK):
						subprocess.call("bash " + filepath, shell=True)
					else:
						# Else, open in vim					
						subprocess.call('vim + -c ":set syntax=markdown" ' + filepath, shell=True)
					sys.exit(0)

