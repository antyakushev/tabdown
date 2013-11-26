import os
import tabdown
if __name__ == "__main__":
    path = "s"
    file = open(os.environ['HOME'] + '/' + path)

    lines = list(filter(lambda x: not x == '', file.read().split('\n'))) #ignore blank lines

    tree = tabdown.parse(lines)
    tabdown.reprint(tree)

