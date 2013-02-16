t - a todolist parser
=====================

t is a personal todolist parser for todo entries in markdown-ish text files.


##Usage:
>t //Prints a formatted list of todo entries
>
>t --now //Prints the current task.

The path of the todolist is by default $HOME/s
By default, t only prints first 4 tasks

The Todo list would look something like this this:

> #Tomorrow

> 	Finish History Paper

> 		Hand it in at 10pm

> 		DO IN LIBRARY!

> 	Finish math hw	

> #Today

> 	Push to Github

> 		Edit Readme!

> 	Read book

> #This line is ignored b/c it doesn't start with tab

> 	Buy rubbing alcohol

> 	Make todo list

> 	This is the 5th item on the list

And the output would look like
> t

> 	Push to Github

> 		Edit Readme!

> 	Read book

> 	Buy rubbing alcohol

> 	Make todo list
