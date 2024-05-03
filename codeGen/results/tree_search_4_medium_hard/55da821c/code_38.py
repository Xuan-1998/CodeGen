def min_replantings(n, m):
    dp = [[float('inf')] * (n + 1) for _ in range(m + 1)]
    dp[0][0] = 0

    for i in range(1, m + 1):
        dp[i][0] = 0
    for j in range(1, n + 1):
        dp[0][j] = j

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if j <= i * m:
                dp[i][j] = min(dp[i-1][k] + (j - k) for k in range(max(0, j-i*m+1), j))
            else:
                dp[i][j] = dp[i-1][j]

    return dp[m][n]
