def minPoints(grid):
    n, m = len(grid), len(grid[0])
    dp = [[float('inf')] * m for _ in range(n)]
    
    # Initialize the base case
    if grid[0][0] > 0:
        dp[0][0] = grid[0][0]
    
    for i in range(1, n):
        for j in range(m):
            if i == 0:  # Only moving right
                dp[i][j] = min(dp[i][j-1], 0) + grid[i][j] if grid[i][j] > 0 else float('inf')
            elif j == 0:  # Only moving down
                dp[i][j] = min(dp[i-1][j], 0) + grid[i][j] if grid[i][j] > 0 else float('inf')
            else:
                dp[i][j] = min(min(dp[i-1][j], dp[i][j-1]), 0) + grid[i][j] if grid[i][j] > 0 else float('inf']
    
    return dp[-1][-1]
