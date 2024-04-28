def coin_paths(k, n, arr):
    dp = [[[0] * (k + 1) for _ in range(n)] for _ in range(n)]
    
    for i in range(n):
        dp[i][0][0] = arr[i][0]
        
    for j in range(n):
        dp[0][j][0] = arr[0][j]
        
    for i in range(1, n):
        for j in range(1, n):
            dp[i][j][0] = arr[i][j]
            
    for i in range(1, n):
        for j in range(1, n):
            for coin in range(min(k, dp[i-1][j][0], dp[i][j-1][0]) + 1):
                if i > 0 and j > 0:
                    dp[i][j][coin] = dp[i-1][j][coin - arr[i][j]] + dp[i][j-1][coin - arr[i][j]]
                elif i == 0:
                    dp[i][j][coin] = dp[0][j-1][coin - arr[i][j]]
                else:
                    dp[i][j][coin] = dp[i-1][j][coin - arr[i][j]]
                    
    return dp[n-1][n-1][k]
