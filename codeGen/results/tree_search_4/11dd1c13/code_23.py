import sys

grid_size = int(input())
grid = []

for _ in range(grid_size):
    row = list(map(int, input().split()))
    grid.append(row)

dp = [[0] * len(grid[0]) for _ in range(grid_size)]

for i in range(1, grid_size):
    for j in range(len(grid[0])):
        dp[i][j] = min(dp[i-1][k] + grid[i][j]) for k in range(j, -1, -1) if i > 0

print(min(sum(row) for row in zip(*dp)))
