#!/usr/bin/env python

import os
import sys
import re
import json
from collections import OrderedDict

#idea: let hashtag mean when!
#tab-delimited ordered tree todolist
#idea: general tab delimited outliner!
#idea: tabdown!

def parse(lines):
    """
    Returns a tree (OrderedDict of OrderedDicts) from a tab-marked list of lines.
    Goes through lines line-by-line.
    """
    tree = OrderedDict()
    levels = [tree]
    for line in lines:
        tabs = lambda line: len(line) - len(line.lstrip('\t'))

        top = levels[-1]

        tabdiff = tabs(line) - len(levels) + 1
        if tabdiff > 0:
            k,v = top.popitem() #pop off last item in top
            top[k] = v #readd it

            levels.append(v) #make it the new highest level
            top = levels[-1] #top = newtop

        if tabdiff < 0:
            for i in range(-1 * tabdiff):
                oldtop = levels.pop()
            top = levels[-1]

        top[line.lstrip('\t')] = OrderedDict()
    return tree

def reprint(tree):
    """
    Prints a tree (OrderedDict of OrderedDicts) marked by tabs 
    Depth-first, recursive traversal of tree
    """
    def _testprint(tree, level):
        if len(tree) == 0:
            return
        for k,v in tree.items():
            print("\t"*level + k)
            _testprint(v, level + 1)
    _testprint(tree, 0)

def main():
    path = "s"
    file = open(os.environ['HOME'] + '/' + path)

    lines = list(filter(lambda x: not x == '', file.read().split('\n'))) #ignore blank lines

    tree = parse(lines)


    print(json.dumps(tree,indent=4))
    reprint(tree)

if len(sys.argv) == 2:
    None
else:
    main()
