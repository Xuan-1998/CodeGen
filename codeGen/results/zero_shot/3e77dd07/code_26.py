class Node:
    def __init__(self, char):
        self.char = char
        self.left = None
        self.right = None

def string_to_tree(s):
    if not s:
        return None

    root = Node(s[0])
    if len(s) > 1:
        root.left = string_to_tree(s[1:])
    if len(s) > 1:
        root.right = string_to_tree(s[2:])

    return root

def tree_to_string(t):
    if not t:
        return ""

    return t.char + tree_to_string(t.left) + tree_to_string(t.right)

def is_scrambled(s1, s2):
    if len(s1) != len(s2):
        return False

    t1 = string_to_tree(s1)
    t2 = string_to_tree(s2)

    def compare_trees(t1, t2):
        if not t1 and not t2:
            return True
        if not t1 or not t2:
            return False
        if t1.char != t2.char:
            return False

        left_match = compare_trees(t1.left, t2.right)
        right_match = compare_trees(t1.right, t2.left)

        return left_match and right_match

    return compare_trees(t1, t2)

# Input from standard input
s1 = input()
s2 = input()

print(is_scrambled(s1, s2))
