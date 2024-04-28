def min_squares(n, m):
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(n + 1):
        for j in range(m + 1):
            if i == 0 or j == 0:
                dp[i][j] = 0
            else:
                s = min(i, j)
                for k in range(1, s + 1):
                    dp[i][j] = min(dp[i][j], dp[i - k][j] + dp[k][j - k])

    return dp[n][m]
