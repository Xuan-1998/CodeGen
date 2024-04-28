def count_paths(K, N, arr):
    dp = [[False] * N for _ in range(N)]
    
    # Base case: reach cell (N-1, N-1)
    dp[N-1][N-1] = (K == 0)
    
    # Fill the DP table
    for i in range(N-2, -1, -1):
        for j in range(N-2, -1, -1):
            if K - arr[i][j] >= 0:
                dp[i][j] = (dp[i+1][j] or dp[i][j+1]) and (K - arr[i][j] == 0)
    
    return int(dp[0][0])
