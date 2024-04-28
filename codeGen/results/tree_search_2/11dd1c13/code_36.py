def minFallingPathSum(grid):
    n = len(grid)
    dp = [[float('inf')] * len(grid[0]) for _ in range(n)]
    
    for j in range(len(grid[0])):
        dp[n-1][j] = grid[n-1][j]
        
    for i in range(n-2, -1, -1):
        for j in range(len(grid[0])):
            min_val = float('inf')
            for k in range(j+1, len(grid[0])):
                min_val = min(min_val, dp[i+1][k] + grid[i][j])
            dp[i][j] = min_val
            
    return min(dp[0])

grid = [[-19,-69,84], [7,15,23],[8,10,14]]
print(minFallingPathSum(grid))
