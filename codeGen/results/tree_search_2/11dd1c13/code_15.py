def minFallingPathSum(grid):
    n = len(grid)
    dp = [[0] * n for _ in range(n)]
    
    # Initialize the first row as is
    for i in range(n):
        dp[0][i] = grid[0][i]
        
    # Fill up the rest of the dp table
    for i in range(1, n):
        for j in range(n):
            if j == 0:
                dp[i][j] = grid[i][j] + min(dp[i-1][k] for k in range(1, n))
            elif j == n - 1:
                dp[i][j] = grid[i][j] + min(dp[i-1][k] for k in range(0, n-1))
            else:
                dp[i][j] = grid[i][j] + min(dp[i-1][k] for k in range(j-1, j+2))
                
    # Return the minimum sum of a falling path
    return min(dp[-1])
