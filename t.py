import os
import sys
from termcolor import colored

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

if len(sys.argv) > 1:
	if sys.argv[1] == '--now':
		for line in lines:
			if line.lstrip() != '' and line[0] == '\t' and line[1] != 't':
				print(line[1:])
				exit()

		exit()

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
exit()
