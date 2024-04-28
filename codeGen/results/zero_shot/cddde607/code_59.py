def coin_path_count(K, N, arr):
    dp = [[[0] * (K + 1) for _ in range(N)] for _ in range(N)]
    
    for i in range(N):
        for j in range(N):
            if i == 0 and j == 0:
                dp[i][j][arr[i][j]] = 1
            elif i > 0 and arr[i-1][j] <= K:
                dp[i][j][arr[i][j]] += dp[i-1][j][K - arr[i][j]]
            elif j > 0 and arr[i][j-1] <= K:
                dp[i][j][arr[i][j]] += dp[i][j-1][K - arr[i][j]]
    return dp[-1][-1][K]
