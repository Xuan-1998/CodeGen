import sys

def are_scrambled(s1, s2):
    if not s1 and not s2:
        return True  # Both strings are empty, so they're scrambled
    if len(s1) != len(s2):
        return False  # Strings have different lengths, so they can't be scrambled

    def build_tree(s):
        if len(s) == 0:
            return None
        mid = len(s) // 2
        left = build_tree(s[:mid])
        right = build_tree(s[mid:])
        return {'val': s[0], 'left': left, 'right': right}

    tree1 = build_tree(s1)
    tree2 = build_tree(s2)

    def is_scrambled(t1, t2):
        if not t1 and not t2:
            return True  # Both trees are empty, so they're scrambled
        if t1['val'] != t2['val']:
            return False  # Characters at corresponding positions don't match
        return (is_scrambled(t1['left'], t2['right']) or
                is_scrambled(t1['right'], t2['left']))

    return is_scrambled(tree1, tree2)

s1 = input()
s2 = input()

print(are_scrambled(s1, s2))
