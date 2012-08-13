#!/usr/bin/env python
#
# t - a todolist parser


import os
import sys
from termcolor import colored

class todo:
	def __init__(self, priority, lines, listname):
		self.priority = priority
		self.lines = lines
		self.listname = listname

class todolist:
	def __init__(self, todos):
		self.todos = todos

	@classmethod
	def fromfile(cls, filepath):
		todomarker = "#Todo:"

		lines = [line.rstrip() for line in open(filepath)]

		isaftertodo = False
		todos = []
		try:
			linebuf = []

			for line in lines:
				if isaftertodo:
					if line.strip() != "":
						numwhitespace = len(line) - len(line.lstrip())
						if numwhitespace < 2:
							if len(linebuf) > 0:
								priority = linebuf[0].strip()[0]
								tempbuf = [linebuf[0].replace(priority, '', 1)]
								tempbuf.extend(linebuf[1:])
								t = todo(priority, tempbuf, filepath)
								todos.append(t)
							linebuf = []
						linebuf.append(line)
				else:
					if line == todomarker:
						isaftertodo = True
			priority = linebuf[0].strip()[0]
			tempbuf = [linebuf[0].replace(priority, '', 1)]
			tempbuf.extend(linebuf[1:])
			t = todo(priority, tempbuf, filepath)
			todos.append(t)
		except IndexError:
			pass

		return cls(todos)

	@classmethod
	def fromfiles(cls, filepaths):
		todos = []
		for filepath in filepaths:
			part = todolist.fromfile(filepath).todos
			todos.extend(part)
		return cls(todos)
	
	def prioritysort(self):
		for todo in self.todos:
			todo.lines[0].replace("'", '~')
		self.todos.sort(key = lambda todo: todo.priority, reverse = True)
		for todo in self.todos:
			todo.lines[0].replace('~', "'")
	def koolprint(self):
		for todo in self.todos:
			color = 'white'
			if todo.priority == '3':
				color = 'blue'
			elif todo.priority == '2':
				color = 'green'
			elif todo.priority == '1':
				color = 'red'
			elif todo.priority == '0':
				color = 'magenta'
			for line in todo.lines:
				print(colored(line, color))
			print("")
	def currenttask(self):
		task = self.todos[len(self.todos)-1].lines[0].strip()
		return task

def main(argv):
	HOME = '/home/slee2/'
	os.chdir(HOME);

	f = open('.t')
	listnames  = []
	for line in f.readlines():
		if line[0] != '#':
			listnames.append(line.strip())
	s = todolist.fromfiles(listnames)
	s.prioritysort()
	
	if len(argv) > 0:
		if argv[0] == 'now':
			print(s.currenttask())
	else:
		s.koolprint()

if __name__ == '__main__':
	main(sys.argv[1:])





