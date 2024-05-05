def calculate_maximum_profit():
    n, m, c0, d0 = map(int, input().split())
    dp = [[0] * (n+1) for _ in range(m+1)]
    
    for i in range(1, m+1):
        ai, bi, ci, di = map(int, input().split())
        
        for j in range(n, c0-1, -1):
            dp[i][j] = max(dp[i-1][j], di + dp[i-1][j-ci-ai])
    
    return dp[m][n]

print(calculate_maximum_profit())
