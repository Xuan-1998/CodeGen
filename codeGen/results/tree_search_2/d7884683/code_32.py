def max_partitions(arr):
    n = len(arr)
    dp = [[0] * (n + 1) for _ in range(n + 1)]

    def dfs(i, j):
        if i == 0 or j == 0:
            return 1
        max_partitions = 0
        for k in range(1, i + 1):
            for m in range(j // (i - k) + 1):
                partitions = min(dfs(k, m), dfs(i - k, j - m))
                if sum(arr[:k]) == sum(arr[k:k+m]):
                    max_partitions = max(max_partitions, partitions + 1)
        return max_partitions

    for i in range(n + 1):
        dp[i][0] = dp[0][i] = 1
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            if sum(arr[:j]) == sum(arr[j:]):
                dp[i][j] = dfs(i, j)
            else:
                dp[i][j] = max(dp[k][m] for k in range(j) for m in range(j // (i - k) + 1))

    return dp[n][n]
