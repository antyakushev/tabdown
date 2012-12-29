Example zsh prompts:
> $		2 hours, 52 minutes

> $		Take a nap



Add this line to your .zsh theme to have your current task show up on the right of your prompt
> RPROMPT='%{$fg[yellow]%}`uptimehr-t`%{$reset_color%}'

You'll also have to add uptimehr-t (and uptimehr), a simple bash script that returns the current task at hand, or your system's uptime. to some folder in your $PATH (eg. $HOME/bin/).



