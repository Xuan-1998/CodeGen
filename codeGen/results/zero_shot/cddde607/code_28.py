def num_paths(arr, K):
    n = len(arr)
    dp = [[[0] * (K+1) for _ in range(n)] for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            if i == 0 and j == 0:
                dp[i][j][0] = arr[i][j]
            elif i > 0 and j == 0:
                dp[i][j][0] = dp[i-1][j][0] + arr[i][j]
            elif i == 0 and j > 0:
                dp[i][j][0] = dp[i][j-1][0] + arr[i][j]
            else:
                dp[i][j][0] = max(dp[i-1][j][0], dp[i][j-1][0]) + arr[i][j]
    
    for i in range(n):
        for j in range(n):
            for k in range(1, K+1):
                if i > 0:
                    dp[i][j][k] = max(dp[i-1][j][k], dp[i][j][k])
                if j > 0:
                    dp[i][j][k] = max(dp[i][j][k], dp[i][j-1][k])
                if i > 0 and j > 0:
                    dp[i][j][k] = max(dp[i-1][j][k], dp[i][j-1][k]) + arr[i][j]
    
    return dp[n-1][n-1][K]
