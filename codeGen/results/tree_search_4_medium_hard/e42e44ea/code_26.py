def minInitialPoints(grid):
    n, m = len(grid), len(grid[0])
    
    # Initialize the dynamic programming table with zeros.
    dp = [[0]*m for _ in range(n)]
    
    # Base case: The minimum points required to reach cell (0, 0) is the value of that cell itself.
    dp[0][0] = grid[0][0]
    
    # Fill up the dynamic programming table from top to bottom and left to right.
    for i in range(1, n):
        for j in range(m):
            if j == 0:
                # For the first column, we can only move from the top cell.
                dp[i][j] = dp[i-1][j] + grid[i][j]
            else:
                # For all other cells, we can either come from the top or left cell.
                dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
    
    # The minimum initial points required to reach the destination cell is stored at dp[n-1][m-1].
    return dp[n-1][m-1]

# Example usage:
grid = [[1, 3], [4, 2]]
n, m = len(grid), len(grid[0])
print(minInitialPoints(grid))  # Output: 5
