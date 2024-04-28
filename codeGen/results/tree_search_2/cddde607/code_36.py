def min_steps_to_collect_k_coins(K, N):
    # Create a 2D DP table where each cell dp[i][j] represents the minimum number of steps needed to reach cell (i, j) with exactly K coins.
    dp = [[[0 for _ in range(K+1)] for _ in range(N)] for _ in range(N)]
    
    # Fill up the DP table by considering all possible moves from each cell.
    for i in range(N):
        for j in range(N):
            if i == 0 and j == 0:
                dp[i][j][K] = arr[0][0] <= K
            else:
                dp[i][j][K] = (dp[max(0, i-1)][j][min(K, arr[i][j])] or 
                               dp[i][max(0, j-1)][min(K, arr[i][j])])
    
    return dp[N-1][N-1][K]
