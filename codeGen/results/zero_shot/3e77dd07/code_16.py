class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def string_to_tree(s):
    if not s:
        return None

    root = Node(s[0])
    nodes = [root]

    for char in s[1:]:
        node = Node(char)
        current_node = nodes.pop(0)
        current_node.left = node
        nodes.append(node)

        if len(nodes) > 0:
            node.right = nodes[0]
            nodes.clear()

    return root

def are_trees_scrambled(t1, t2):
    if not t1 and not t2:
        return True

    if not t1 or not t2:
        return False

    left_match = are_trees_scrambled(t1.left, t2.left)
    right_match = are_trees_scrambled(t1.right, t2.right)

    if left_match and right_match:
        return True
    else:
        # swap the children of t1
        temp = t1.left
        t1.left = t1.right
        t1.right = temp

        return are_trees_scrambled(t1, t2)

def is_scrambled(s1, s2):
    t1 = string_to_tree(s1)
    t2 = string_to_tree(s2)

    return are_trees_scrambled(t1, t2)

# Test the solution
s1 = "abc"
s2 = "cab"

print(is_scrambled(s1, s2))  # Output: True

s1 = "abc"
s2 = "bac"

print(is_scrambled(s1, s2))  # Output: False
