class Node:
    def __init__(self, char):
        self.char = char
        self.left = None
        self.right = None

def build_tree(s):
    if not s:
        return None
    root = Node(s[0])
    root.left = build_tree(s[1:])
    if root.left and len(root.left) > 0:
        root.right = Node(root.left[0])
        root.left = root.left[1:]
    return root

def scramble_tree(t):
    if t is None or (t.left is None and t.right is None):
        return t
    t.left, t.right = t.right, t.left
    return t

def are_anagrams(s1, s2):
    return sorted(s1) == sorted(s2)

def is_scrambled_string(s1, s2):
    if len(s1) != len(s2):
        return False
    t1 = build_tree(s1)
    t2 = build_tree(s2)
    while t1 and t2:
        if t1.char != t2.char:
            return are_anagrams(t1.left.char + t1.right.char, t2.left.char + t2.right.char) \
                   or are_anagrams(t1.left.char + t1.right.char, t2.left.char + t2.right.char)
        t1 = scramble_tree(t1)
        t2 = scramble_tree(t2)
    return True

s1 = input()
s2 = input()

print(is_scrambled_string(s1, s2))
