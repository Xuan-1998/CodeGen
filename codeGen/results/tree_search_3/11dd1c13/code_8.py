def minFallingPathSum(grid):
    n = len(grid)
    
    dp = [[0] * n for _ in range(n)]
    
    for i in range(n):
        dp[i][0] = grid[i][0]
        
    for j in range(1, n):
        prev_min = float('inf')
        for k in range(n):
            if j == 0:
                break
            min_val = dp[i][j-1] + grid[i][k]
            dp[i][j] = min(dp[i][j], min_val)
            prev_min = min(prev_min, min_val)
    return min(dp[-1])

