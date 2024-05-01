def count_ways(m, N):
    dp = [[0] * (N + 1) for _ in range(m + 1)]
    
    for i in range(1, m + 1):
        for j in range(i, N + 1):
            if i == 1:
                dp[i][j] = 1
            else:
                for k in range(j - 1):
                    dp[i][j] += dp[i-1][k]
    
    return (dp[m][N] % (10**9+7))
