import sys

def binary_tree(s):
    if len(s) == 0:
        return None
    mid = len(s) // 2
    left = s[:mid]
    right = s[mid:]
    node = {'left': binary_tree(left), 'right': binary_tree(right)}
    return node

def compare_trees(t1, t2):
    if t1 is None and t2 is None:
        return True
    if t1 is None or t2 is None:
        return False
    left_match = compare_trees(t1['left'], t2['right'])
    right_match = compare_trees(t1['right'], t2['left'])
    return left_match and right_match

def is_scrambled(s1, s2):
    t1 = binary_tree(s1)
    t2 = binary_tree(s2)
    return compare_trees(t1, t2)

s1 = sys.stdin.readline().strip()
s2 = sys.stdin.readline().strip()
print(is_scrambled(s1, s2))
