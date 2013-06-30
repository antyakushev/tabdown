#!/usr/bin/env python
from subprocess import Popen, PIPE
from random import choice

ESPEAK_CMD = "ssh osh.it.cx 'espeak --stdout -s 150|aplay -t wav -'"
NAME = "Sean"

# Populate tasks
tasks = Popen(["/home/slee2/.bin/t --list"], shell=True, stdout=PIPE).communicate()[0].decode('utf-8').split('\n')[:-1]

# Expand tasks
def expand(task):
	mydict = {
			'hw': 'homework',
			'520': 'multivariable',
			}
	for k in mydict.keys():
		task = task.replace(k, mydict[k]);
[expand(task) for task in tasks]


# Sentence blocks
greeting = [
		'Hey ' + NAME + '!',
		NAME + ',',
		'Yo ' + NAME + '!', 
		]
idle = [
		'You should populate your todo list!',
		'What should you really be doing right now?',
		'Are you really done with your tasks for today?',
		'Add stuff to your todo list!',
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

# Generate sentence
def generate(tasks):
	out = []
	if len(tasks) == 0:
		out.append(choice(greeting))
		out.append(choice(idle))
	elif len(tasks) == 1:
		out.append(choice(greeting))
		out.append(choice(ask)(tasks[0]))
	elif len(tasks) == 2:
		out.append(choice(greeting))
		out.append(choice(ask)(tasks[0]))
		out.append(choice(dontforget))
		out.append(tasks[-1] + '.')
	if len(tasks) > 2:
		out.append(choice(greeting))
		out.append(choice(ask)(tasks[0]))
		out.append(choice(dontforget))
		[out.append(task + ',') for task in tasks[1:-2]]
		out.append(tasks[-2] + ', and')
		out.append(tasks[-1] + '.')
	return ' '.join(out)

generated = generate(tasks)

# Say Sentence
def say(s):
	p = Popen([ESPEAK_CMD], shell=True, stdin=PIPE)
	p.communicate(input=bytes(s, 'utf-8'))
say(generated)
