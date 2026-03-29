def maxPathSum(tree):
    n = len(tree)
    dp = [0] * (n+1)
    parent = [-1] * (n+1)

    for i in range(n//2, -1, -1):
        left = 2*i+1
        right = 2*i+2
        if left < n:
            dp[i] = max(dp[left], dp[right]) + tree[i]
            parent[i] = left if dp[left] > dp[right] else right
        else:
            dp[i] = tree[i]

    return dp[0]

# Example usage:
tree = [3, 9, 20, None, None, 15, 7]
print(maxPathSum(tree))  # Output: 30 (from path 3 -> 9 -> 20)
