import sys

def is_scrambled(s1, s2):
    # Create binary trees for s1 and s2
    tree1 = create_tree(s1)
    tree2 = create_tree(s2)

    # Compare the tree structures of s1 and s2
    if compare_trees(tree1, tree2):
        return True
    else:
        return False

def create_tree(s):
    # Base case: an empty string is a leaf node
    if len(s) == 0:
        return None

    # Recursive case: partition the string into two non-empty substrings
    mid = len(s) // 2
    left = s[:mid]
    right = s[mid:]

    # Create nodes for the left and right subtrees
    node_left = create_tree(left)
    node_right = create_tree(right)

    # Return a node with the left and right subtrees as children
    return {'value': s, 'left': node_left, 'right': node_right}

def compare_trees(t1, t2):
    # Base case: both trees are empty (i.e., they represent an empty string)
    if t1 is None and t2 is None:
        return True

    # Recursive case: compare the values of the nodes
    if t1['value'] != t2['value']:
        return False

    # Compare the left subtrees
    if not compare_trees(t1['left'], t2['right']):
        return False

    # Compare the right subtrees
    if not compare_trees(t1['right'], t2['left']):
        return False

    # If we reach this point, the trees are identical
    return True

# Read input strings from stdin
s1 = sys.stdin.readline().strip()
s2 = sys.stdin.readline().strip()

# Determine if s2 is a scrambled string of s1
result = is_scrambled(s1, s2)

# Print the result to stdout
print(result)
