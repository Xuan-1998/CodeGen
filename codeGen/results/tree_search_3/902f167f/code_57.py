def min_tiles(n, m):
    if n == 0 or m == 0:
        return 0
    
    dp = [[float('inf')] * (m + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if i < j:
                dp[i][j] = min(dp[i][j], dp[i][i] + dp[i - 1][j - i])
            elif j < i:
                dp[i][j] = min(dp[i][j], dp[i][i] + dp[i][j - 1])
    
    return dp[n][m]

n, m = map(int, input().split())
print(min_tiles(n, m))
