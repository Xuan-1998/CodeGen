def min_path_sum(grid):
    m, n = len(grid), len(grid[0])
    dp = [[0] * n for _ in range(m)]

    # Initialize the first row and column of the dp array
    for i in range(1, m):
        dp[i][0] = grid[i][0] + dp[i-1][0]
    for j in range(1, n):
        dp[0][j] = grid[0][j] + dp[0][j-1]

    # Fill in the rest of the dp array
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = grid[i][j] + min(dp[i-1][j], dp[i][j-1])

    return dp[m-1][n-1]

# Example usage:
grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(min_path_sum(grid))  # Output: 12
