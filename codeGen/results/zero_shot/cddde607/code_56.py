def count_paths(K, N, arr):
    dp = [[[0] * (K + 1) for _ in range(N)] for _ in range(N)]
    
    for i in range(N):
        for j in range(N):
            if i == 0 and j == 0:
                dp[i][j][arr[i][j]] = 1
            else:
                if i > 0:
                    dp[i][j][arr[i][j]] += dp[i-1][j][arr[i-1][j]]
                if j > 0:
                    dp[i][j][arr[i][j]] += dp[i][j-1][arr[i][j-1]]
    
    return dp[N-1][N-1][K]
