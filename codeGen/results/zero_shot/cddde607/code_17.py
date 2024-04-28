def count_paths(k, n, arr):
    dp = [[[0] * (k + 1) for _ in range(n)] for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            if i == 0 and j == 0:
                dp[i][j][0] = arr[i][j]
            elif i == 0:
                dp[i][j][:k+1] = [dp[i][j-1][i] + arr[i][j] for i in range(k+1)]
            elif j == 0:
                dp[i][j][:k+1] = [dp[i-1][j][i] + arr[i][j] for i in range(k+1)]
            else:
                dp[i][j][:k+1] = [[min(dp[i-1][j][i], dp[i][j-1][i]) + arr[i][j] for i in range(k+1)]]
    
    return dp[-1][-1][-1]
