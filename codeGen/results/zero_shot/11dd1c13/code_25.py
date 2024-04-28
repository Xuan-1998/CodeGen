import sys
grid = [list(map(int, line.split())) for line in sys.stdin.readlines()]
dp = [[0] * (len(grid[0]) + 1) for _ in range(len(grid) + 1)]
for i in range(1, len(grid)):
    for j in range(1, len(grid[0])):
        dp[i][j] = max(min(dp[i-1][k] for k in range(j)) or float('inf'), min(dp[i-1][k] for k in range(j+1))) + grid[i][j]
print(min(dp[-1]))
