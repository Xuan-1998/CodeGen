def countPaths(K, N, arr):
    dp = [[[0] * (K+1) for _ in range(N)] for _ in range(N)]
    
    dp[0][0][0] = 1
    for i in range(1, N):
        for j in range(i+1):
            if arr[i][j] <= K:
                dp[i][j][arr[i][j]] += dp[i-1][j][arr[i-1][j]]
                dp[i][j][K] += dp[i-1][j][min(K, arr[i-1][j])]
    
    return dp[N-1][N-1][K]
