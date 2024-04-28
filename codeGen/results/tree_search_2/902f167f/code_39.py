def minSquares(n, m):
    dp = [[float('inf')] * (m + 1) for _ in range(n + 1)]
    dp[0][:] = [0] * (m + 1)
    dp[:, 0] = [0] * (n + 1)

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            min_val = float('inf')
            for s in range(1, min(i, j) + 1):
                if (i - s) * (j - s) > 0:
                    min_val = min(min_val, dp[i - s][j] + dp[i][j - s])
            dp[i][j] = min_val + 1

    return dp[n][m]

n, m = map(int, input().split())
print(minSquares(n, m))
