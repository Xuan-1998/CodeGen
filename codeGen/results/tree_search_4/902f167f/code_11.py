def min_squares(n, m):
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if i <= j:
                dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + 1
            else:
                min_squares = float('inf')
                for k in range(1, i+1):
                    if (i % k == 0) and (j % k == 0):
                        min_squares = min(min_squares, dp[k-1][j//k] + dp[i//k-1][j%k] + 1)
                dp[i][j] = min_squares

    return dp[n][m]

n, m = map(int, input().split())
print(min_squares(n, m))
