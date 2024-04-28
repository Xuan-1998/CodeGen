def min_squares(n, m):
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(n + 1):
        for j in range(m + 1):
            if i == 0 or j == 0:
                dp[i][j] = 1
            else:
                dp[i][j] = min({dp[k][j] + (i - k) for k in range(min(i, j), -1, -1)}) + (min(i, j) != 0)

    return dp[n][m]
