def count_ways(m, n):
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    for k in range(1, m + 1):
        dp[0][k] = 1

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if i > 0:
                dp[i][j] = sum(dp[i-1][k] for k in range(1, j+1))
            else:
                dp[i][j] = 1 if j == 1 else 0

    return dp[n][m]
