from collections import defaultdict

def find_lis(arr):
    n = len(arr)
    dp = [[0] * (n + 1) for _ in range(n + 1)]

    memo = defaultdict(dict)

    def dfs(i, j):
        if (i, j) in memo:
            return memo[(i, j)]
        if j == 0:
            return 1
        if i > 0 and arr[i - 1] <= arr[i]:
            dp[i][j] = dfs(i - 1, j)
        else:
            dp[i][j] = max(dfs(i - 1, k) for k in range(j + 1)) + 1
        memo[(i, j)] = dp[i][j]
        return dp[i][j]

    max_lis_length = 0

    for i in range(n):
        for j in range(1, n + 1):
            max_lis_length = max(max_lis_length, dfs(i, j))

    return max_lis_length
