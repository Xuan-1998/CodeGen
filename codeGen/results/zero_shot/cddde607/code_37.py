def count_paths(K, N, arr):
    dp = [[[0] * (K + 1) for _ in range(N)] for _ in range(N)]
    
    for i in range(N):
        dp[i][0][0] = arr[i][0]
        
    for j in range(N):
        dp[0][j][0] = arr[0][j]
        
    for i in range(1, N):
        for j in range(1, N):
            dp[i][j][0] = max(dp[i-1][j][0], dp[i][j-1][0])
            
    for k in range(1, K + 1):
        for i in range(N):
            for j in range(N):
                if arr[i][j] <= k:
                    dp[i][j][k] = max(dp[(i-1)][j][k-arr[i][j]], dp[i][(j-1)][k-arr[i][j]]) + 1
                else:
                    dp[i][j][k] = dp[min(i, N-1)][j][k]
                    
    return dp[-1][-1][-1]
