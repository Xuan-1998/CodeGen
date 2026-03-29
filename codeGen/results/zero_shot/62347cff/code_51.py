def min_path_sum(grid):
    m = len(grid)
    n = len(grid[0])
    
    # Initialize a 2D array to store the minimum sum of all numbers along paths from (0, 0) to each cell.
    dp = [[0] * n for _ in range(m)]
    
    # Base case: The minimum sum of all numbers along the path to the top left corner is the value at that corner.
    dp[0][0] = grid[0][0]
    
    # Calculate the minimum sum of all numbers along paths from (0, 0) to each cell in the first row.
    for j in range(1, n):
        dp[0][j] = dp[0][j-1] + grid[0][j]
    
    # Calculate the minimum sum of all numbers along paths from (0, 0) to each cell in the first column.
    for i in range(1, m):
        dp[i][0] = dp[i-1][0] + grid[i][0]
    
    # Calculate the minimum sum of all numbers along paths from (0, 0) to each cell in the rest of the grid.
    for i in range(1, m):
        for j in range(1, n):
            # The minimum sum of all numbers along a path to a cell is the minimum of the sums of all numbers along paths to the cells above and to the left, plus the value at that cell.
            dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
    
    # The minimum sum of all numbers along the path from the top left corner to the bottom right corner is stored in the last cell.
    return dp[m-1][n-1]

# Example usage:
grid = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]
print(min_path_sum(grid))  # Output: 7
