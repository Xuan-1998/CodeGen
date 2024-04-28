def count_paths(K, N, arr):
    dp = [[[0]*(K+1) for _ in range(N)] for _ in range(N)]
    
    for i in range(N):
        for j in range(N):
            if i == 0 and j == 0:
                if arr[i][j] <= K:
                    dp[i][j][arr[i][j]] = 1
                else:
                    dp[i][j][K] = 0
    
    for i in range(1, N):
        for j in range(N):
            for k in range(K+1):
                if arr[i][j] <= k:
                    dp[i][j][k] = dp[i-1][j][k-arr[i][j]] + dp[i][j-1][k-arr[i][j]]
                else:
                    dp[i][j][k] = dp[i-1][j][k]
    
    return dp[-1][-1][K]
