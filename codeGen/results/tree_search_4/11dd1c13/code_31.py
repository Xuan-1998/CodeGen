def minFallingPathSum(grid):
    n = len(grid)
    dp = [[0] * n for _ in range(n)]
    
    # Initialize dp[0][j] as grid[0][j] for each j
    for j in range(n):
        dp[0][j] = grid[0][j]
        
    # Fill up the table in a bottom-up manner
    for i in range(1, n):
        for j in range(n):
            if i == 1:
                dp[i][j] = min(dp[0][k] + grid[i][j]) for k in range(n) if k != j
            else:
                dp[i][j] = min(dp[i-1][k] + grid[i][j]) for k in range(n) if k != j
    
    # Return the minimum sum of a path ending at the bottom row
    return min(dp[-1])
