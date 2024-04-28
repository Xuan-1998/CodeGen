def num_paths_to_collect_k_coins(k, n, arr):
    dp = [[[0] * (k + 1) for _ in range(n)] for _ in range(n)]
    
    dp[0][0][0] = 1
    
    for i in range(1, n):
        for j in range(1, n):
            if arr[i][j] <= k:
                dp[i][j][arr[i][j]] += dp[i-1][j][arr[i-1][j]] + dp[i][j-1][arr[i][j-1]][arr[i][j]]
    
    return dp[-1][-1][k]
