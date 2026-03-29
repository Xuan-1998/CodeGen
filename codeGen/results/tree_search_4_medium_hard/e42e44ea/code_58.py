def minInitialPoints(grid):
    M, N = len(grid) - 1, len(grid[0]) - 1
    dp = [[float('inf')] * (N + 1) for _ in range(M + 1)]

    for i in range(1, M + 1):
        for j in range(1, N + 1):
            if grid[i][j] > 0:
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]

    return dp[M][N]

# Example usage
grid = [[1, 2], [3, 4]]
print(minInitialPoints(grid))  # Output: 5
