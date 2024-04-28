def countPaths(K, N, arr):
    dp = [[[0] * (K + 1) for _ in range(N)] for _ in range(N)]
    
    dp[0][0][0] = arr[0][0]
    
    for i in range(1, N):
        dp[i][0][0] = max(dp[i-1][0][0], dp[i-1][i][0]) + arr[i][0]
        dp[0][i][0] = max(dp[0][i-1][0], dp[i][i-1][0]) + arr[0][i]
    
    for i in range(1, N):
        for j in range(1, N):
            if arr[i][j] <= K:
                dp[i][j][K] = max(dp[i-1][j][K], dp[i][j-1][K]) + arr[i][j]
    
    return dp[N-1][N-1][K]
