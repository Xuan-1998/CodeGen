def min_squares(n, m):
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(n + 1):
        dp[i][0] = 1

    for j in range(m + 1):
        dp[0][j] = 1

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if (i * i) <= j:
                dp[i][j] = min(dp[i - 1][j], dp[i][j - j]) + 1
            else:
                dp[i][j] = dp[i][j - 1] + 1

    return dp[n][m]

n, m = map(int, input().split())
print(min_squares(n, m))
