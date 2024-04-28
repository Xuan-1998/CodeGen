def numPaths(arr, K, N):
    dp = [[[0] * (K + 1) for _ in range(N)] for _ in range(N)]
    
    dp[0][0][0] = arr[0][0]
    
    for i in range(1, N):
        dp[i][0][0] = dp[i-1][0][0] + arr[i][0]
        
    for j in range(1, N):
        dp[0][j][0] = dp[0][j-1][0] + arr[0][j]
        
    for i in range(1, N):
        for j in range(1, N):
            if arr[i][j] <= K:
                dp[i][j][arr[i][j]] += 1
            if i > 0 and dp[i-1][j][K-arr[i][j]]:
                dp[i][j][K] += dp[i-1][j][K-arr[i][j]]
            if j > 0 and dp[i][j-1][K-arr[i][j]]:
                dp[i][j][K] += dp[i][j-1][K-arr[i][j]]
                
    return dp[N-1][N-1][K]
