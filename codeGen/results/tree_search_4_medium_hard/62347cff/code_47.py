code
from typing import List

def minPathSum(grid: List[List[int]]) -> int:
    m, n = len(grid), len(grid[0])
    
    # Create the dp array with all values initialized to infinity
    dp = [[float('inf')] * n for _ in range(m)]
    
    # Base cases: The first row and column of the grid
    for i in range(m):
        dp[i][0] = grid[i][0]
    for j in range(n):
        dp[0][j] = grid[0][j]
    
    # Fill up the rest of the dp array using the state expression
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
    
    return dp[m-1][n-1]

# Example usage:
grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(minPathSum(grid))  # Output: 12
