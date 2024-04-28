def count_paths(K, N, arr):
    dp = [[[0] * (K + 1) for _ in range(N)] for _ in range(N)]
    
    for i in range(N):
        for j in range(N):
            if i == 0 and j == 0:
                dp[i][j][0] = arr[i][j]
            else:
                if i > 0:
                    dp[i][j][0] += dp[i-1][j][0]
                if j > 0:
                    dp[i][j][0] += dp[i][j-1][0]
    
    for k in range(1, K + 1):
        for i in range(N):
            for j in range(N):
                if i > 0 and dp[i-1][j][k-1] > 0:
                    dp[i][j][k] += dp[i-1][j][k-1]
                if j > 0 and dp[i][j-1][k-1] > 0:
                    dp[i][j][k] += dp[i][j-1][k-1]
    
    return dp[N-1][N-1][K]
