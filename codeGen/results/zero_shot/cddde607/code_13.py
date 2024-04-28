def coin_paths(k, n, arr):
    dp = [[0] * (n+1) for _ in range(n+1)]
    
    for i in range(1, n+1):
        dp[i][0] = 0
        dp[0][i] = 0
    
    for i in range(1, n+1):
        for j in range(1, n+1):
            if arr[i-1][j-1] <= k:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1]) + (arr[i-1][j-1] == 0)
            else:
                dp[i][j] = 0
    
    return dp[n][n]
