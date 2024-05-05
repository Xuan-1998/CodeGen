def maxPathSum(root):
    def dfs(node):
        if not node:
            return 0
        left = max(0, dfs(node.left))
        right = max(0, dfs(node.right))
        nonlocal max_sum
        max_sum = max(max_sum, left + right + node.val)
        return node.val + max(left, right)

    max_sum = float('-inf')
    dfs(root)
    return max_sum

if __name__ == "__main__":
    root = [4, 2, 5, 1, 3]
    print(maxPathSum(root))
