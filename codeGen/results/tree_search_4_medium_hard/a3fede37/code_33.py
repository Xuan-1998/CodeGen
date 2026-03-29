class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def max_path_sum(tree):
    # Convert the binary tree to a list representation
    tree_list = []
    stack = [(tree, 0)]
    while stack:
        node, index = stack.pop()
        if node is not None:
            tree_list.append(node.value)
            stack.extend([(node.right, index*2+1), (node.left, index*2+2)])
        else:
            tree_list.append(None)

    # Calculate the maximum sum of a path for each node
    n = len(tree_list) - 1
    dp = [0] * n

    for i in range(n):
        if tree_list[i]:
            left_sum = 0 if tree_list[2*i+1] is None else dp[2*i]
            right_sum = 0 if tree_list[2*i+2] is None else dp[2*i+1]
            dp[i] = max(tree_list[i], tree_list[i]+left_sum, tree_list[i]+right_sum)

    # Return the maximum sum of a path in the given binary tree
    return max(dp)
