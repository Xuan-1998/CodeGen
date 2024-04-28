def count_paths(K, N, arr):
    dp = [[[0] * (K + 1) for _ in range(N)] for _ in range(N)]
    
    for i in range(N):
        for j in range(N):
            if i == 0 and j == 0:
                dp[i][j][arr[i][j]] = 1
            else:
                for k in range(arr[i][j], K + 1):
                    if i > 0:
                        dp[i][j][k] += dp[i - 1][j][k - arr[i][j]]
                    if j > 0:
                        dp[i][j][k] += dp[i][j - 1][k - arr[i][j]]
    
    return dp[-1][-1][K]
