import sys
from collections import deque

def minFallingPathSum(grid):
    m = len(grid)
    dp = [[0] * m for _ in range(m)]
    
    # Base case: fill the first row with the corresponding values from the grid
    for j in range(m):
        dp[0][j] = grid[0][j]
        
    # Fill the rest of the table using dynamic programming
    for i in range(1, m):
        for j in range(m):
            if i == 1:
                dp[i][j] = min(dp[i-1][:]) + grid[i][j]
            else:
                dp[i][j] = min(dp[i-1][:j] + [grid[i][j]]) + grid[i][j]
                
    return min(dp[-1])

# Read the input
m = int(input())
grid = []
for _ in range(m):
    row = list(map(int, input().split()))
    grid.append(row)

print(minFallingPathSum(grid))
