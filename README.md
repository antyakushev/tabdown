t - a todolist parser
=====================

t is a todolist parser for todo entries in markdown text files.

t supports a simple task classification system
>	3 not urgent, not important
>
>	2 not urgent, important
>
>	1 urgent, important
>
>	0 current

Now how do I balance work and play? With t (hopefully)...

##Usage:
>t //Prints a formatted list of todo entries
>
>t --now //Prints the current task.
#Dependencies
- termcolor module for python

##Installation
- Copy t to some folder in your $PATH (eg. $HOME/bin)
- Copy s, the example todolist, to your $HOME directory


##Todo:
- Make it support only one todo list (eg. no need to edit code)-
	Support default values for certain things
- Add enviormental variables (MODE=Weekend MODE=Weekday)
	- Bug: parse until next #
	- Bug: tnow doesn't work
- Make it export the current task as an environmental variable
- Colorize README, fix example code formatting with inline HTML

