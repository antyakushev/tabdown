t - a todolist system
=====================

t is a todolist system designed to be unintrusive, quick and powerful.

The todo list's path by default $HOME/s. 

t, the program, begins parsing the todolist after the keyword "#Today" (Look at the sample "s" file and its "sampleoutput" for a basic idea). 
By default, t only prints the first 4 tasks.


##Usage:
>t //Prints a formatted list of todo entries
>
>t --now //Prints the current task, useful to pipe to other programs. I pipe it to a statusbar to keep me on track


##Installation
Add t to your a directory in your $PATH like $HOME/bin.

Add the sample 's' file to your $HOME directory.

###if you use vim:
Add this to your .vimrc to log finished tasks with F3:

>nmap \<F3\> dd:echo system('str="$(date +"%F %H:%M")";str="$str$(echo '.shellescape(@").')";echo $str \>\> done')\<CR\>:echo 'Nice Job!'\<CR\>

