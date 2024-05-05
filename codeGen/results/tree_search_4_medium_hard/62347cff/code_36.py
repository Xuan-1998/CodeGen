def minPathSum(grid):
    m, n = len(grid), len(grid[0])
    dp = [[float('inf')] * n for _ in range(m)]

    dp[0][0] = grid[0][0]
    for i in range(1, m):
        dp[i][0] = dp[i-1][0] + grid[i][0]
    for j in range(1, n):
        dp[0][j] = dp[0][j-1] + grid[0][j]

    for i in range(1, m):
        for j in range(1, n):
            if i > 0 and j > 0:
                dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
            else:
                if i == 0:
                    dp[i][j] = dp[0][j-1] + grid[i][j]
                elif j == 0:
                    dp[i][j] = dp[i-1][0] + grid[i][j]

    return dp[m-1][n-1]

# Example usage
grid = [[1,3,1],[1,5,1],[4,2,1]]
print(minPathSum(grid))  # Output: 7
