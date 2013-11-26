def parse(lines):
    """Returns tree from a tab-structured list of lines
    Populates tree line by line.

    example:

    These lines

    a
        b
        c
            d
    e

    will be stored as (commas omitted):

    (None [
        (a [
            (b [])
            (c [
                (d [])
            ])
        ])
        (e [])
    ])

    """
    tree = (None, []) #root node
    levels = [tree]
    for line in lines:
        if line == '':
            pass
        tabs = lambda line: len(line) - len(line.lstrip('\t'))

        top = levels[-1]
        tabdiff = tabs(line) - len(levels) + 1
        if tabdiff > 0:
            levels.append(top[1][-1])
            top = levels[-1]
        if tabdiff < 0:
            for counter in range(-1 * tabdiff):
                    levels.pop()
            top = levels[-1]
        top[1].append( (line.lstrip('\t'), []) )
    return tree

def reprint(tree):
    """Prints a tab-structured list of lines corresponding to a given tree
    Does a recursive depth first traversal of tree.

    example:

    This tree (commas omitted)

    (None [
        (a [
            (b [])
            (c [
                (d [])
            ])
        ])
        (e [])
    ])

    will be printed as

    a
        b
        c
            d
    e

    """
    def _reprint(node, level):
        if len(node[1]) == 0:
            return
        for child in node[1]:
            print("\t"*level + child[0])
            _reprint(child, level + 1)
    _reprint(tree, 0)
