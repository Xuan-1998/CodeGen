def minSquares(n, m):
    dp = [[float('inf')] * (m + 1) for _ in range(n + 1)]
    dp[0][0] = 0

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            for s in range(1, min(i, j) + 1):
                if i - s >= 0 and j - s >= 0:
                    dp[i][j] = min(dp[i][j], dp[i - s][j - s] + 1)

    return dp[n][m]

n, m = map(int, input().split())
print(minSquares(n, m))
