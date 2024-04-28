from sys import stdin

grid = [[int(x) for x in line.split()] for line in stdin.readlines()]

dp = [[0] * len(grid[0]) for _ in range(len(grid))]

for i in range(1, len(grid)):
    dp[i][0] = grid[i][0]
    for j in range(1, len(grid[0])):
        dp[i][j] = min(dp[i-1][k] for k in range(j)) + grid[i][j]

print(min(dp[-1]))
