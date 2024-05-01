import sys
from collections import deque

# Read input from stdin
grid = [list(map(int, input().split())) for _ in range(int(input()))]

# Initialize dynamic programming table
n = len(grid)
dp = [[0] * n for _ in range(n)]

# Base case: dp[0][j] = grid[0][j]
for j in range(n):
    dp[0][j] = grid[0][j]

# Tabulation
for i in range(1, n):
    for j in range(n):
        if i > 0:
            min_sum = float('inf')
            for k in range(j):
                min_sum = min(min_sum, dp[i-1][k])
            dp[i][j] = grid[i][j] + min_sum
        else:
            dp[i][j] = grid[i][j]

# Print the minimum sum of a falling path with non-zero shifts
min_sum = float('inf')
for j in range(n):
    min_sum = min(min_sum, dp[-1][j])
print(min_sum)
