def min_path_sum(grid):
    m, n = len(grid), len(grid[0])
    
    # Create a 2D array to store the minimum sum of paths ending at each cell
    dp = [[0] * n for _ in range(m)]
    
    # Initialize the first row and column of the DP table
    dp[0][0] = grid[0][0]
    for i in range(1, m):
        dp[i][0] = dp[i-1][0] + grid[i][0]
    for j in range(1, n):
        dp[0][j] = dp[0][j-1] + grid[0][j]
    
    # Fill up the rest of the DP table
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
    
    return dp[m-1][n-1]

# Example usage:
grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(min_path_sum(grid))  # Output: 12
