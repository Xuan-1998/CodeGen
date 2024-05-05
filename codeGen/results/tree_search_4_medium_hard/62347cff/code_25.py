import sys
from typing import List

def min_path_sum(grid: List[List[int]]) -> int:
    m, n = len(grid), len(grid[0])
    
    # Initialize the dynamic programming table with initial values of infinity
    dp = [[0] * n for _ in range(m)]
    
    # Base cases are dp[0][j] = dp[i][0] = 0 for all i and j, since we can't move up from the top boundary or left from the left boundary.
    for i in range(m):
        dp[i][0] = 0
    for j in range(n):
        dp[0][j] = 0
    
    # Fill the dynamic programming table based on the optimal substructure
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
    
    return dp[m-1][n-1]
