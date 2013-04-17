#!/usr/bin/env python
import os
import sys
from termcolor import colored

def print_now():
	for line in lines:
		if line.lstrip() != '' and line[0] == '\t' and line[1] != 't':
			print(line[1:])
			break

def print_list():
	for line in lines:
		if line.lstrip() != '' and line[0] == '\t' and line[1] != 't':
			print(line[1:])

def print_colored():
	colors = ['blue', 'green', 'red', 'cyan']
	counter = len(colors)

	for line in lines:
		if line.lstrip() != '' and line[0] == '\t':
				if line[1] != '\t':
					counter -= 1
					print('')
					if counter < 0:
						exit()
				print(colored(line,colors[counter]))
	print('')

os.chdir(os.environ['HOME'])
filepath = "s"
lines = []
start = False


for line in open(filepath):
	line = line.rstrip()
	if start:
		lines.append(line)
	if line == '#Today':
		start = True

functions = {
		'--now': print_now,
		'--list': print_list,
		}
if len(sys.argv) == 2:
	functions[sys.argv[1]]()
else:
	print_colored()
