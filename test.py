import os
from tabdown import indexmap
if __name__ == "__main__":
    path = "s"
    file = open(os.environ['HOME'] + '/' + path)

    lines = list(filter(lambda x: not x == '', file.read().split('\n'))) #ignore blank lines

    tree = indexmap.genindextree(lines)

    indexmap.reprint(lines, tree)

