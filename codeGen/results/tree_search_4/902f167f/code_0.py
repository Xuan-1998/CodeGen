def min_squares(n, m):
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            for k in range(1, min(i, j) + 1):
                dp[i][j] = min(dp[i][j], dp[i - k][j - k] + 1)

    return dp[n][m]

n, m = map(int, input().split())
print(min_squares(n, m))
