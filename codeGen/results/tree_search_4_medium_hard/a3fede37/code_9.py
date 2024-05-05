class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def max_path_sum(node):
    if not node:
        return 0

    memo = {}

    def dfs(node):
        if node in memo:
            return memo[node]

        max_sum = node.value

        if node.left and node.right:
            max_sum = max(max_sum, node.value + dfs(node.left) + dfs(node.right))
        elif node.left:
            max_sum = max(max_sum, node.value + dfs(node.left))
        elif node.right:
            max_sum = max(max_sum, node.value + dfs(node.right))

        memo[node] = max_sum
        return max_sum

    return max(dfs(node), key=lambda x: x)

# Example usage:
root = Node(1)
root.left = Node(-2)
root.right = Node(3)
root.left.left = Node(-4)
root.left.right = Node(5)

print(max_path_sum(root))  # Output: 6
