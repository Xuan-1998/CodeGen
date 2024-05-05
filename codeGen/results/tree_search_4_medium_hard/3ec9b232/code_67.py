def count_ways(M):
    n = len(M)
    MOD = 10**9 + 7
    
    dp = [[0] * (n+1) for _ in range(n+1)]
    
    for i in range(n+1):
        dp[i][0] = 1
    
    for j in range(1, n+1):
        for i in range(j-1, -1, -1):
            for k in range(i+1, j+1):
                dp[j][k] = (dp[j][k] + dp[j-1][i]) % MOD
    
    return dp[n][n]
