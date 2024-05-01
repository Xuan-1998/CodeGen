def iter_dp(n, m):
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            # calculate dp[i][j] using previously computed values
            # ...
    return min(dp[n][m])
