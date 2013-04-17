#!/usr/bin/env python
from subprocess import Popen, PIPE
from random import choice

ESPEAK_CMD = "ssh osh.it.cx 'espeak --stdout|aplay -t wav -'"
NAME = "Sean"

tasks = Popen(["t --list"], shell=True, stdout=PIPE).communicate()[0].decode('utf-8').split('\n')[:-1]

def say(s):
	p = Popen([ESPEAK_CMD], shell=True, stdin=PIPE)
	p.communicate(input=bytes(s, 'utf-8'))

#Generate Sentence
greeting = [
		'Hey ' + NAME + '!',
		NAME + ',',
		'Yo ' + NAME + '!', 
		]
ask = [
		lambda x: 'Did you ' + x + ' yet?',
		lambda x: 'You better ' + x + ' now!',
		lambda x: 'Please ' + x + ' now!',
		]
dontforget = [
		"Don't forget to",
		"Also, Don't forget to",
		]

out = []
out.append(choice(greeting))
out.append(choice(ask)(tasks[0]))
if len(tasks) > 2:
	out.append(choice(dontforget))
	[out.append(task + ',') for task in tasks[1:-2]]
	out.append(tasks[-2] + ', and')
	out.append(tasks[-1] + '.')
elif len(tasks) > 1:
	out.append(choice(dontforget))
	out.append(tasks[-1] + '.')


output = ' '.join(out)
print(output)
say(output)
