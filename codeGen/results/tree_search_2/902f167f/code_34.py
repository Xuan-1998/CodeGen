def min_squares(n, m):
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if i < 2 or j < 2:
                dp[i][j] = 1
            else:
                min_squares = float('inf')
                for k in range(1, min(i, j) + 1):
                    min_squares = min(min_squares, dp[i - k][j - k] + (i // k) * (j // k))
                dp[i][j] = min_squares

    return dp[n][m]
