def min_squares(n, m):
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if i == 1 or j == 1:
                dp[i][j] = max(i, j)
            else:
                min_squares = float('inf')
                for k in range(j):
                    min_squares = min(min_squares, dp[i-1][j-k-1] + 1)
                dp[i][j] = min_squares

    return dp[n][m]
