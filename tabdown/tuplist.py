"""
a
    b
    c
        d

[
    (a [
        (b [])
        (c [
            (d [])
        ])
    ])
]
"""
#make this for tuple/list tree data structure
def parse(lines):
	tree = (None, []) #root node
	levels = [tree]
	for line in lines:
		tabs = lambda line: len(line) - len(line.lstrip('\t'))

		top = levels[-1]
		tabdiff = tabs(line) - len(levels) + 1
		if tabdiff > 0:
			"""
			levels.append(last element in top)
			top = levels[-1]
			"""
			levels.append(top[1][-1])
			top = levels[-1]
		if tabdiff < 0:
			for counter in range(-1 * tabdiff):
				levels.pop()
			top = levels[-1]
		top[1].append( (line.lstrip('\t'), []) )
	return tree

def reprint(tree):
    def _reprint(node, level):
        if len(node[1]) == 0:
            return
        for child in node[1]:
            print("\t"*level + child[0])
            _reprint(child, level + 1)
    _reprint(tree, 0)

if __name__ == "__main__":
	test = ["a", "\tb", "\tc","\t\td","e"]
	print(parse(test))
	reprint(parse(test))
