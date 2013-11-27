import os
import json
import tabdown
if __name__ == "__main__":
    path = "s"
    file = open(os.environ['HOME'] + '/' + path)

    lines = file.readlines()

    tree = tabdown.markdown(lines)
    print(json.dumps(tree, indent=4))
