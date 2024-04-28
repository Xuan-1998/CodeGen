def count_paths(K, N, arr):
    dp = [[[0] * (K + 1) for _ in range(N)] for _ in range(N)]
    
    dp[0][0][0] = 1
    
    for i in range(1, N):
        for j in range(i+1):
            for k in range(K + 1):
                if arr[i][j] <= k:
                    dp[i][j][k] = dp[i-1][j][k-arr[i][j]] + dp[i-1][j][k]
                else:
                    dp[i][j][k] = dp[i-1][j][k]
                    
    return dp[-1][-1][K]
