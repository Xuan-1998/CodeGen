def count_paths(K, N, arr):
    dp = [[[0] * (K + 1) for _ in range(N)] for _ in range(N)]
    
    for i in range(N):
        dp[i][0][0] = 1
    
    for i in range(1, N):
        for j in range(1, N):
            if arr[i][j] <= K:
                dp[i][j][K] += dp[i-1][j][K-arr[i][j]] + dp[i][j-1][K-arr[i][j]]
    
    return dp[N-1][N-1][K]
