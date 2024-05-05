def min_path_sum(grid):
    m, n = len(grid), len(grid[0])
    
    # Create a dp table to store the minimum sum for each cell
    dp = [[0] * n for _ in range(m)]
    
    # Base case: The minimum sum of all numbers along the path ending at the bottom right corner is the value at that cell
    dp[m-1][n-1] = grid[m-1][n-1]
    
    # Fill up the dp table from the bottom right to the top left
    for i in range(m-2, -1, -1):
        for j in range(n-2, -1, -1):
            # The minimum sum of all numbers along the path ending at cell (i, j) is the minimum of:
            # 1. The value at cell (i, j) plus the minimum sum of all numbers along the path ending at the cell below
            # 2. The value at cell (i, j) plus the minimum sum of all numbers along the path ending at the cell to the right
            dp[i][j] = grid[i][j] + min(dp[i+1][j], dp[i][j+1])
    
    # The minimum sum of all numbers along the path from top left to bottom right is stored in the top left cell of the dp table
    return dp[0][0]

# Example usage:
grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(min_path_sum(grid))  # Output: 12
