def minFallingPathSum(grid):
    n = len(grid)
    dp = [[0] * n for _ in range(n)]

    # Initialize the first row as the grid itself
    dp[0] = grid[0]

    for i in range(1, n):
        for j in range(n):
            if j == 0:
                dp[i][j] = min(dp[i-1][:]) + grid[i][j]
            elif j == n - 1:
                dp[i][j] = min([dp[i-1][k] + grid[i][j] for k in range(n)]) 
            else:
                dp[i][j] = min([dp[i-1][k] + grid[i][j] for k in range(n)]) 

    return min(dp[-1])

grid = [[1,-4,7], [10, -2, 8]]
print(minFallingPathSum(grid)) # Output: 6
