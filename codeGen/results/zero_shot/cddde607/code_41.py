def count_paths(K, N, arr):
    dp = [[[0] * (K + 1) for _ in range(N)] for _ in range(N)]
    
    dp[0][0][0] = arr[0][0]
    
    for i in range(1, N):
        for j in range(i+1):
            if j == 0:
                dp[i][j][0] = dp[i-1][j][0] + arr[i][j]
            elif j == i:
                dp[i][j][0] = dp[i-1][j-1][0] + arr[i][j]
            else:
                dp[i][j][0] = max(dp[i-1][j][0], dp[i-1][j-1][0]) + arr[i][j]
    
    for k in range(1, K+1):
        for i in range(N):
            for j in range(i+1):
                if j == 0:
                    dp[i][j][k] = dp[i-1][j][k-1] if dp[i-1][j][k-1] >= arr[i][j] else 0
                elif j == i:
                    dp[i][j][k] = dp[i-1][j-1][k-1] if dp[i-1][j-1][k-1] >= arr[i][j] else 0
                else:
                    dp[i][j][k] = max(dp[i-1][j][k-1], dp[i-1][j-1][k-1]) if (dp[i-1][j][k-1] + dp[i-1][j-1][k-1]) >= arr[i][j] else 0
    
    return dp[N-1][N-1][K]
