import re
from collections import OrderedDict

def genindextree(lines):
    """
    Returns a tree (OrderedDict of OrderedDicts) of line indicies from a tab-marked list of lines.
    Goes through lines line-by-line.
    """
    _lines = enumerate(lines)
    tree = OrderedDict()
    levels = [tree]
    for i,line in _lines:
        tabs = lambda line: len(line) - len(line.lstrip('\t'))

        top = levels[-1]

        tabdiff = tabs(line) - len(levels) + 1
        if tabdiff > 0:
            k,v = top.popitem() #pop off last item in top
            top[k] = v #readd it

            levels.append(v) #make it the new highest level
            top = levels[-1] #top = newtop

        if tabdiff < 0:
            for counter in range(-1 * tabdiff):
                oldtop = levels.pop()
            top = levels[-1]

        top[str(i)] = OrderedDict()
    return tree

def reprint(lines, tree):
    """
    Prints a tree (OrderedDict of OrderedDicts) marked by tabs 
    Depth-first, recursive traversal of tree
    """
    def _reprint(tree, level):
        if len(tree) == 0:
            return
        for k,v in tree.items():
            print("\t"*level + lines[int(k)].lstrip('\t'))
            _reprint(v, level + 1)
    _reprint(tree, 0)
