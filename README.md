#tabdown
_tabdown is for humans!_

Write trees with as little syntactic overhead as possible!

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
- markup for humans, by humans: inspired by _Markdown_ and _YAML_

###install
```
npm install tabdown
```

###usage
```javascript
var tabdown = require('tabdown');
var lines = [ 
  '#shopping list',
  '\tsoy sauce',
  '\tonions',
  '\teggs',
  '',
  '#todo',
  '\teat',
  '\tsleep',
  '\tplay/work',
  '\t',
  '' ];


var tree = tabdown.parse(lines, '\t');
console.log(tree);
/*
{ data: null,
  depth: -1,
  parent: null,
  children: 
   [ { data: '#shopping list',
       depth: 0,
       parent: [Circular],
       children: [Object],
       tabcount: 0 },
     { data: '#todo',
       depth: 0,
       parent: [Circular],
       children: [Object],
       tabcount: 0 } ] }
*/
tabdown.print(tree);
/*
#shopping list
	soy sauce
	onions
	eggs
#todo
	eat
	sleep
	play/work
*/

tabdown.traverse(tree, function(node) { console.log(node.depth, node.data)});
/*
0 '#shopping list'
1 'soy sauce'
1 'onions'
1 'eggs'
0 '#todo'
1 'eat'
1 'sleep'
1 'play/work'
*/
```
