def minSquares(n, m):
    dp = [[float('inf')] * (m + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if (i ** 0.5) == int((i ** 0.5)):
                dp[i][j] = min(dp[i][j], 1)
            else:
                for k in range(1, min(i, j) + 1):
                    if i >= k and j >= k:
                        dp[i][j] = min(dp[i][j], dp[i - k][j - k] + 1)
    
    return dp[n][m]

n, m = map(int, input().split())
print(minSquares(n, m))
