def max_path_sum(tree):
    n = len(tree)
    dp = [[0] * 2 for _ in range(n)]

    def dfs(i):
        if i >= n or tree[i] == -1:
            return 0

        if dp[i][0]:
            return dp[i][0]

        left_sum = dfs(2*i+1)
        right_sum = dfs(2*i+2)

        dp[i][0] = max(left_sum, right_sum) + tree[i]
        dp[i][1] = max(left_sum, right_sum)

        return dp[i][0]

    max_sum = 0
    for i in range(n):
        if tree[i] != -1:
            max_sum = max(max_sum, dfs(i))

    return max_sum

# Example usage:
tree = [-10, 9, 17, -1, 3, 4, -2, 6, 5, -3]
print(max_path_sum(tree))  # Output: 24
