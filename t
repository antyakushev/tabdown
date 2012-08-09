#!/usr/bin/env python
#
# t - a todo parser

#TODO: Create a class containter for a todo entry
# What about too many todo list items? should I only show the top 3?
import os
import sys
import operator
from termcolor import colored


HOME = '/home/slee2/'
os.chdir(HOME);

# Parse strings
def parse_after_todo(path):
	todomarker = "##Todo:"


	lines = [line.rstrip() for line in open(path)]

	# Significant lines and their child lines  are put in the buf list, joined, then added to tasks list
	isaftertodo = False
	tasks = [] # List of line groups
	buf = []

	for line in lines:
		if isaftertodo:
			if line.strip() != "":
				# Treats anything with more than leading two wspace chars as child strings
				numwspace = len(line) - len(line.lstrip())
				if numwspace < 2:
					if len(buf) > 0:
						# debug
						tasks.append(buf)
					buf = []

				buf.append(line.replace("'", '~'))
		else:
			if line == todomarker:
				isaftertodo = True
	tasks.append(buf)  # append whatever is leftover

	return tasks

def todoformat(str):
	spaces = len(str) - len(str.lstrip())
	
	if str[spaces].isdigit():
		return colored(str[:spaces+1], 'magenta') + str[spaces+1:]
	else:
		return str



filepaths = [entry.strip() for entry in open(HOME+ '.t')]

# t (no args) - display aggregated todo-list
if len(sys.argv) == 1:
	alltodos = []  #List of tuples containing list of todo strings and a filepath

	lengthoflongestfp = 0;
	for filepath in filepaths:
		if filepath[0] != '#':  ## if not a comment
			# Get longest filepath ( for latter formatting)
			if len(filepath) > lengthoflongestfp:
				lengthoflongestfp = len(filepath)
			# Add todo entries from each file to alltodos[]
			for todo in parse_after_todo(filepath):
				if len(todo) > 0:
					alltodos.append([filepath, todo])

	alltodos.sort(key = operator.itemgetter(1), reverse = True)  # reverse alpha sort on todo text 

	for todo in alltodos[:len(alltodos) - 1]:
		fp = todo[0]  # first val in tuple is filepath
		lines = todo[1]  # second val in tuple is text

		ljustnum = lengthoflongestfp + 2
		spaces = ''.join([' ' for num in xrange(ljustnum)])
		print(colored(fp, 'blue') + spaces[len(fp):] + todoformat(lines[0].replace('~', "'")))
		for line in lines[1:]:
			print(todoformat(spaces + line.replace('~', "'")))

		print("")
	for todo in alltodos[len(alltodos) - 1:]:
		fp = todo[0]  # first val in tuple is filepath
		lines = todo[1]  # second val in tuple is text

		ljustnum = lengthoflongestfp + 2
		spaces = ''.join([' ' for num in xrange(ljustnum)])
		print(colored(fp, 'blue') + spaces[len(fp):] + todoformat(colored(lines[0].replace('~', "'"), 'green')))
		for line in lines[1:]:
			print(todoformat(spaces + colored(line.replace('~', "'"), 'green')))

		print("")


else:
	if sys.argv[1] == 'ls':
		#filepaths.sort(key = lambda x: os.path.getmtime(x))
		#filepaths.reverse()
		for file in filepaths:
			print(colored(file, 'blue'))

		

