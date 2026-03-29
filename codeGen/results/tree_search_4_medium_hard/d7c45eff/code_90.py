def min_string(n, k):
    dp = [[0] * (k + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, min(i, k) + 1):
            if j <= k:
                dp[i][j] = min(dp[i-1][j-1], dp[i-1][j])
            else:
                dp[i][j] = s[:i]

    return dp[n][k]
