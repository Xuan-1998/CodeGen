def count_paths(k, n, arr):
    dp = [[[0] * (k + 1) for _ in range(n)] for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            if i == 0 and j == 0:
                if arr[i][j] <= k:
                    dp[i][j][arr[i][j]] = 1
            elif i > 0 and j > 0:
                if arr[i][j] <= k:
                    dp[i][j][arr[i][j]] = dp[i - 1][j][arr[i-1][j-1]] + dp[i][j-1][arr[i][j-1]]
            elif i > 0 and j == 0:
                if arr[i][j] <= k:
                    dp[i][j][arr[i][j]] = dp[i - 1][j][arr[i-1][j]]
            else:
                if arr[i][j] <= k:
                    dp[i][j][arr[i][j]] = dp[i][j-1][arr[i][j-1]]
    
    return dp[n-1][n-1].count(1)
