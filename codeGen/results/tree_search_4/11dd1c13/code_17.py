def minFallingPathSum(grid):
    grid_size = len(grid)
    
    for i in range(1, grid_size):
        for j in range(grid_size):
            if j == 0:
                left = grid[i-1][j]
            elif j == grid_size - 1:
                right = grid[i-1][j]
            else:
                left = grid[i-1][j-1]
                right = grid[i-1][j+1]
            
            if i < grid_size - 1:
                if j > 0 and j < grid_size - 1:
                    dp[i][j] = min(dp[i-1][k] + grid[i][j]) for all k such that 0 <= k < j and k != j - 1
                else:
                    dp[i][j] = min(left, right) + grid[i][j]
            else:
                if j == 0:
                    dp[i][j] = left + grid[i][j]
                elif j == grid_size - 1:
                    dp[i][j] = right + grid[i][j]
                else:
                    dp[i][j] = min(left, right) + grid[i][j]

    return min(dp[grid_size-1])
