def numPathsWithKCoins(K, N, arr):
    dp = [[0] * (N) for _ in range(N)]
    
    # Edge case: If K or N is less than 1, return 0
    if K < 1 or N < 1:
        return 0
    
    # Fill dp[][] from top-down manner according to the transition relationship
    for i in range(N):
        for j in range(N):
            if i == 0 and j == 0:
                if arr[i][j] <= K:
                    dp[i][j] = 1
                else:
                    dp[i][j] = 0
            elif i > 0 and j > 0:
                if arr[i][j] <= K:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
                else:
                    dp[i][j] = max(0, dp[i-1][j], dp[i][j-1])
            elif i > 0 and j == 0:
                if arr[i][j] <= K:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = 0
            elif i == 0 and j > 0:
                if arr[i][j] <= K:
                    dp[i][j] = dp[i][j-1]
                else:
                    dp[i][j] = 0
    
    # Return the number of ways to reach the bottom-right corner
    return dp[N-1][N-1]
