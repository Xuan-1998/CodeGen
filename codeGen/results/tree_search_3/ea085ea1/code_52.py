def find_max_common_substrings():
    str1 = input().strip()
    str2 = input().strip()

    max_length = 0
    common_substrings = set()
    tree_root = None

    for i in range(len(str1)):
        for j in range(i + 1, len(str1) + 1):
            substring = str1[i:j]
            if substring in str2:
                if len(substring) > max_length:
                    max_length = len(substring)
                    common_substrings = {substring}
                    tree_root = TreeNode(substring, None, None)
                elif len(substring) == max_length and substring not in common_substrings:
                    common_substrings.add(substring)

    # Initialize the tree
    current_node = tree_root

    for substring in common_substrings:
        if subtree_root is None:
            subtree_root = TreeNode(substring, None, None)
            current_node.left = subtree_root
            current_node.right = subtree_root
        else:
            if len(substring) > max_length:
                current_node.left = TreeNode(substring, None, None)
                current_node.right = TreeNode(substring, None, None)
            else:
                if substring not in common_substrings:
                    common_substrings.add(substring)

    # Traverse the tree to find the maximum number of non-overlapping substrings
    max_count = 0

    def traverse_tree(node):
        nonlocal max_count
        if node is None:
            return 0
        count = traverse_tree(node.left) + 1
        if count > max_count:
            max_count = count
        count += traverse_tree(node.right)
        return count

    return traverse_tree(tree_root)

class TreeNode:
    def __init__(self, substring, left=None, right=None):
        self.substring = substring
        self.left = left
        self.right = right
