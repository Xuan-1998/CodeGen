import sys
from collections import deque

# Read the grid from stdin
grid = [list(map(int, input().split())) for _ in range(int(input()))]

# Initialize the dp table with zeros and set the base case for the first row
dp = [[0] * len(grid[0]) for _ in range(len(grid))]
for j in range(len(grid[0])):
    dp[0][j] = grid[0][j]

# Fill up the dp table using dynamic programming
for i in range(1, len(grid)):
    queue = deque([(0, 0)])
    while queue:
        k, j = queue.popleft()
        for c in set(range(len(grid[0]))):
            if (k - 1 >= 0) and (j - 1 < 0 or j == c):
                dp[i][c] = min(dp[i-1][k-1] + grid[i][c], dp[i-1][k] + grid[i][c])
        for k in range(len(grid)):
            if k > 0:
                queue.append((k, j))

# Find the minimum sum of a falling path with non-zero shifts
min_sum = sys.maxsize
for c in set(range(len(grid[0]))):
    min_sum = min(min_sum, dp[-1][c] + grid[-1][c])

print(min_sum)
