import os
import tabdown
if __name__ == "__main__":
    path = "s"
    file = open(os.environ['HOME'] + '/' + path)

    lines = file.readlines()

    tree = tabdown.parse(lines)
    tabdown.reprint(tree)

