import sys

grid = []
while True:
    try:
        line = list(map(int, input().split()))
        grid.append(line)
    except EOFError:
        break

dp = [[0] * len(grid[0]) for _ in range(len(grid))]

for i in range(1, len(grid)):
    for j in range(len(grid[0])):
        dp[i][j] = min(dp[i-1][max(0, j-grid[i-1][k]) - 1] + grid[i][j] for k in range(len(grid[0]))) if i > 0 else 0

min_sum = min(dp[-1])
print(min_sum)
