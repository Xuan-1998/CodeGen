import sys
from collections import deque

# Read the grid size and initialize the dynamic programming table
grid_size = int(input())
dp = [[0] * grid_size for _ in range(grid_size)]

# Initialize the queue with the top-left cell
queue = deque([(0, 0, grid[0][0])])
dp[0][0] = grid[0][0]

# Perform BFS to fill up the dynamic programming table
while queue:
    i, j, val = queue.popleft()
    
    # For each cell in the current row
    for k in range(j + 1, grid_size):
        dp[i][k] = min(dp[i][k], dp[i - 1][k - 1] + val)
        
    # For each cell in the previous row
    if i > 0:
        for k in range(grid_size):
            if k != j:  # Ignore cells in the same column
                queue.append((i - 1, k, dp[i - 1][k] + grid[i][j]))
                
# The minimum sum of a falling path with non-zero shifts is stored in the bottom-right cell
print(dp[-1][-1])
