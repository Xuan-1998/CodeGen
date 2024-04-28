def findPaths(N, K, arr):
    dp = [[0] * (K + 1) for _ in range(N)]
    
    # Base case: dp[N-1][N-1] = 1 if arr[N-1][N-1] == K and 0 otherwise.
    dp[N-1][K] = 1 if arr[N-1][N-1] == K else 0

    for i in range(N-2, -1, -1):
        for j in range(K+1):
            # If the current cell has coins, we can either collect them or not.
            dp[i][j] = (dp[i][j] + dp[i+1][min(j, arr[i][N-1])]) if i < N-1 else 0
            
            # We also need to consider the previous column. 
            # If the current cell's value is less than or equal to K, we can collect coins from this cell.
            dp[i][j] += (dp[i][min(j, arr[i][N-1])]) if j >= arr[i][N-1] else 0

    return dp[0][K]
