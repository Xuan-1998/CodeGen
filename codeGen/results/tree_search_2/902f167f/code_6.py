def min_tiles(n, m):
    dp = [[float('inf')] * (m + 1) for _ in range(n + 1)]
    
    for i in range(n + 1):
        for j in range(m + 1):
            if i == 0 or j == 0:
                dp[i][j] = 0
            else:
                for k in range(min(i, j) + 1):
                    dp[i][j] = min(dp[i][j], dp[i-k][j-k] + 1)
    
    return dp[n][m]

n, m = map(int, input().split())
print(min_tiles(n, m))
