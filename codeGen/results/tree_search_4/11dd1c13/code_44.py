def minFallingPathSum(grid):
    n = len(grid)
    dp = [[float('inf')] * n for _ in range(n)]
    
    for j in range(n):
        dp[0][j] = grid[0][j]
        
    for i in range(1, n):
        for j in range(n):
            min_sum = float('inf')
            for k in range(n):
                if abs(j - k) == i:
                    min_sum = min(min_sum, dp[i-1][k] + grid[i][j])
            dp[i][j] = min_sum
            
    return min(dp[-1])

# Test the function
grid = [[2,1,3],[5,2,1]]
print(minFallingPathSum(grid))
