def min_squares(n, m):
    dp = [[float('inf')] * (m + 1) for _ in range(n + 1)]

    # Base case - Single cells
    for i in range(n + 1):
        dp[i][0] = 1
    for j in range(m + 1):
        dp[0][j] = 1

    # Transition relationship
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            for k in range(i):
                for m in range(j):
                    if (i - k) * (j - m) ** 0.5 == int((i - k) * (j - m) ** 0.5):
                        dp[i][j] = min(dp[i][j], dp[k][m] + 1)

    return dp[n][m]
