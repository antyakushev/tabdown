#tabdown
_tabdown is for humans!_

Express trees with as little syntactic overhead as possible!

Read trees with as little linguistic overhead as possible!

###what
Tabdown is an ultra-minimalist markup language for describing trees. It uses leading tabs as a structuring character.

###examples
####a contrived todo list
```
I need to
	eat
		lunch
		dinner
	sleep

I want to
	browse the web
	read a book

```

####finding prime factorizations
```
72
	12
		4
			2
			2
		3
	6
		3
		2
```

###inspiration
- whitespace as information carriers: inspired by _Python_
- markup for humans, by humans: inspired by _Markdown_
- data markup: inspired by _JSON_

##todo:
- fix reprint2
- port to method 2 instead of method 1 (more room for semantic info, move to json
- make python generator for callback, perline info population


- port to javascript
 - markdown converter
 - html converter
- make functionally extensible; give it callbacks
- reprogram t to use tabdown


