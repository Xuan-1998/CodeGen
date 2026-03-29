import sys

def string_to_tree(s):
    if not s:
        return None
    root = Node(s[0])
    current = root
    for char in s[1:]:
        if len(current.children) < 2:
            current.children.append(Node(char))
            current = current.children[-1]
        else:
            current = current.children[0]
            while len(current.children) == 2:
                current = current.children[0]
            current.children.append(Node(char))
    return root

def tree_to_string(root):
    if not root:
        return ""
    result = []
    stack = [root]
    while stack:
        node = stack.pop()
        if node.children:
            stack.extend(node.children)
        else:
            result.append(node.val)
    return "".join(map(str, result))

class Node:
    def __init__(self, val):
        self.val = val
        self.children = []

def is_scrambled(s1, s2):
    t1 = string_to_tree(s1)
    t2 = string_to_tree(s2)
    return tree_to_string(t1) == tree_to_string(t2)

s1 = input().strip()
s2 = input().strip()

print(is_scrambled(s1, s2))
