def min_squares(n, m):
    dp = [[float('inf')] * (m + 1) for _ in range(n + 1)]
    dp[0][j] = 1 if j == 0 else float('inf')
    dp[i][0] = 1 if i == 0 else float('inf')

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if max(i, j) % min(i, j) == 0:
                dp[i][j] = min(dp[i][j], dp[i - max(i, j)][j - 1])
            else:
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + 1

    return dp[n][m]

n, m = map(int, input().split())
print(min_squares(n, m))
