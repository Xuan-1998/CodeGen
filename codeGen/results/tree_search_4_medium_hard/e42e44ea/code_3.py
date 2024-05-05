def minInitialPoints(grid):
    n, m = len(grid), len(grid[0])
    dp = [[float('inf')] * (m + 1) for _ in range(n + 1)]
    
    # Initialize the starting state (top-left cell)
    dp[0][0] = grid[0][0]
    
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if grid[i-1][j-1] > 0:
                # If the current point is positive, we can move from either above or to the left
                dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i-1][j-1]
            else:
                # If the current point is negative, we must subtract 1 and take the maximum of the two possible paths
                dp[i][j] = max(dp[i-1][j]-1, dp[i][j-1]-1) - abs(grid[i-1][j-1])
    
    return dp[-1][-1]
