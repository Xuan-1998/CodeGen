class TreeNode:
    def __init__(self, char):
        self.char = char
        self.left = None
        self.right = None

def string_to_tree(s):
    if not s:
        return None
    root = TreeNode(s[0])
    queue = [root]
    i = 1
    while i <= len(s):
        node = queue.pop(0)
        if i < len(s):
            node.left = TreeNode(s[i])
            queue.append(node.left)
            i += 1
        if i < len(s):
            node.right = TreeNode(s[i])
            queue.append(node.right)
            i += 1
    return root

def are_trees_scrambled(t1, t2):
    if not t1 and not t2:
        return True
    if not t1 or not t2:
        return False
    if t1.char != t2.char:
        return False
    return are_trees_scrambled(t1.left, t2.left) and are_trees_scrambled(t1.right, t2.right)

s1_tree = string_to_tree(s1)
s2_tree = string_to_tree(s2)
is_scrambled = are_trees_scrambled(s1_tree, s2_tree)
print(is_scrambled)
