def maxPathSum(tree):
    def dfs(node):
        if dp[node] is not None:
            return dp[node]

        left_sum = right_sum = -float('inf')
        if 2*node+1 < len(tree): 
            left_sum = dfs(2*node+1)
        if 2*node+2 < len(tree):
            right_sum = dfs(2*node+2)

        dp[node] = tree[node]
        if left_sum > 0:
            dp[node] = max(dp[node], tree[node] + left_sum)
        if right_sum > 0:
            dp[node] = max(dp[node], tree[node] + right_sum)

        return dp[node]

    dp = [None]*len(tree)
    return max(dfs(0), key=lambda x: x)
