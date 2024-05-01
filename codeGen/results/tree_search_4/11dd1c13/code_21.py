def minFallingPathSum(grid):
    grid_size = len(grid)
    dp = [[0] * grid_size for _ in range(grid_size)]

    dp[0][0] = grid[0][0]
    for i in range(1, grid_size):
        for j in range(grid_size):
            if i > 0:
                min_sum = float('inf')
                for k in range(j, -1, -1):
                    if k >= 0 and k < grid_size:
                        min_sum = min(min_sum, dp[i-1][k] + grid[i][j])
                dp[i][j] = min_sum

    return min(dp[-1])

grid = [[1, 2], [4, 3]]
print(minFallingPathSum(grid))  # Output: 7
