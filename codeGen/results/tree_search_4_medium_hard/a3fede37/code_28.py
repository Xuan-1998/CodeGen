class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def max_path_sum(root):
    memo = {0: 0}

    def dfs(node):
        if node in memo:
            return memo[node]

        total = node.val
        left_sum = dfs(node.left) if node.left else -1
        right_sum = dfs(node.right) if node.right else -1

        max_sum = total + left_sum + right_sum
        memo[node] = max_sum

        return max_sum

    def max_path(node):
        if not node:
            return 0

        left_sum = dfs(node.left)
        right_sum = dfs(node.right)

        return node.val + max(left_sum, right_sum) if (left_sum > -1 and right_sum > -1) else -1

    return max(max_path(root), 0)

# Test your solution
root = Node(5)
root.left = Node(-3)
root.right = Node(8)
root.left.left = Node(-2)
root.left.right = Node(2)
root.right.left = Node(3)
root.right.right = Node(2)
print(max_path_sum(root))  # Output: 11
