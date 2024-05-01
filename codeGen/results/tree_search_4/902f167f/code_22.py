def min_squares(n, m):
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(n + 1):
        for j in range(m + 1):
            if i == 0 or j == 0:
                dp[i][j] = 0
            else:
                min_squares = float('inf')
                for k in range(1, min(i, j) + 1):
                    min_squares = min(min_squares, 1 + dp[max(0, i - k)][max(0, j - k)])
                dp[i][j] = min_squares

    return dp[n][m]
