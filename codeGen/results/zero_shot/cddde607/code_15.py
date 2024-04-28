def count_paths(K, N, arr):
    dp = [[[0] * (K + 1) for _ in range(N)] for _ in range(N)]
    
    for i in range(N):
        for j in range(N):
            if i == 0 and j == 0:
                dp[i][j][0] = arr[i][j]
            elif i == 0:
                dp[i][j][0] = dp[i][j-1][0] + arr[i][j]
            elif j == 0:
                dp[i][j][0] = dp[i-1][j][0] + arr[i][j]
            else:
                dp[i][j][0] = max(dp[i-1][j][0], dp[i][j-1][0]) + arr[i][j]
            
            for k in range(1, K+1):
                if i == 0 and j == 0:
                    dp[i][j][k] = (arr[i][j] == k)
                elif i == 0:
                    dp[i][j][k] = dp[i][j-1][k] + (arr[i][j] == k)
                elif j == 0:
                    dp[i][j][k] = dp[i-1][j][k] + (arr[i][j] == k)
                else:
                    dp[i][j][k] = max(dp[i-1][j][k], dp[i][j-1][k]) + (arr[i][j] == k)
    
    return dp[N-1][N-1][K]
