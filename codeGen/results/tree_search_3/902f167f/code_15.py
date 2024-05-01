def min_squares(n, m):
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            min_squares = float('inf')
            for k in range(min(i, j), 0, -1):
                l = max(1, (i - k) // k * k)
                min_squares = min(min_squares, dp[i - k][j] + dp[k][l])
            dp[i][j] = min_squares

    return dp[n][m]

n, m = map(int, input().split())
print(min_squares(n, m))
