def num_paths_to_collect_k_coins(k, n, arr):
    dp = [[[0] * (k + 1) for _ in range(n)] for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            if i == 0 and j == 0:
                dp[i][j][0] = arr[i][j]
            elif i == 0:
                dp[i][j][0] = dp[i][j-1][0] + arr[i][j]
            elif j == 0:
                dp[i][j][0] = dp[i-1][j][0] + arr[i][j]
            else:
                dp[i][j][0] = max(dp[i-1][j][0], dp[i][j-1][0]) + arr[i][j]
            
    return dp[-1][-1][k]
