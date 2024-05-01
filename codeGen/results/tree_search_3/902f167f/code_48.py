def min_squares(n, m):
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(n + 1):
        for j in range(m + 1):
            if i == 0 or j == 0:
                dp[i][j] = 1
            elif i > 0 and j > 0:
                dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + (i * j) % 2

    return dp[n][m]
