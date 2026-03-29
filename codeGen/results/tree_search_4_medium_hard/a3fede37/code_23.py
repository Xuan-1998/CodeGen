class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def max_path_sum(root):
    memo = {}

    def dfs(node):
        if node is None:
            return 0
        
        if node in memo:
            return memo[node]
        
        left_sum = dfs(node.left)
        right_sum = dfs(node.right)

        current_max = node.val
        if left_sum > 0 and right_sum > 0:
            current_max += max(left_sum, right_sum) + node.val

        memo[node] = current_max
        return current_max

    return max(dfs(root.left), dfs(root.right)) + root.val
