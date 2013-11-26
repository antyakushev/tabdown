def parse(lines):
    """Returns tree from a tab-structured list of lines
    Populates tree line by line.
    """

    tree = {"children": []}
    levels = [tree]
    for line in lines:
        if line.strip() == "": #ignore blank lines
            continue

        tabs = lambda line: len(line) - len(line.lstrip('\t'))

        top = levels[-1]
        tabdiff = tabs(line) - len(levels) + 1
        if tabdiff > 0:
            top["children"][-1]["children"] = []
            levels.append(top["children"][-1])
        elif tabdiff < 0:
            for counter in range(-1 * tabdiff):
                levels.pop()
        top = levels[-1]
        node = {
                "text": line.lstrip('\t').rstrip(),
                }
        top["children"].append(node)
    return tree

def reprint(tree):
    """Prints a tab-structured list of lines corresponding to a given tree
    Does a recursive,  depth-first traversal of tree.
    """
    def _reprint(node, level):
        if not "children" in node.keys():
            return
        for child in node['children']:
            print("\t"*level + child["text"])
            _reprint(child, level + 1)
    _reprint(tree, 0)
