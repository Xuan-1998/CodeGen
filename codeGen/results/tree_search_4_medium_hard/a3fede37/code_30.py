def maxPathSum(root):
    def dfs(node):
        if not node:
            return 0

        left_sum = max(0, dfs(node.left))
        right_sum = max(0, dfs(node.right))

        current_sum = node.val + left_sum + right_sum

        dp[node] = current_sum
        return current_sum

    dp = {}
    return dfs(root)
