def is_scrambled(s1, s2):
    # Convert both strings into binary trees
    def treeify(s):
        if not s:
            return None
        mid = len(s) // 2
        return {'left': treeify(s[:mid]), 'right': treeify(s[mid:])}

    t1 = treeify(s1)
    t2 = treeify(s2)

    # Compare the two binary trees node by node
    def compare_trees(t1, t2):
        if not t1 and not t2:
            return True
        if not t1 or not t2:
            return False
        if t1['left'] != t2['left']:
            return False
        if t1['right'] != t2['right']:
            return False
        return compare_trees(t1['left'], t2['left']) and compare_trees(t1['right'], t2['right'])

    return compare_trees(t1, t2)

# Test the function
s1 = input()
s2 = input()
print(is_scrambled(s1, s2))
