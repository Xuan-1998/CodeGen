import sys

n = int(sys.stdin.readline().strip())
grid = []
for _ in range(n):
    row = list(map(int, sys.stdin.readline().strip().split()))
    grid.append(row)

dp = [[0] * n for _ in range(n)]
dp[0] = [row[0] for row in grid]

for i in range(1, n):
    for j in range(n):
        if j == 0:
            dp[i][j] = dp[i-1][j] + grid[i][j]
        else:
            dp[i][j] = min(dp[i-1][k] for k in range(n)) + grid[i][j]

print(min(dp[-1]))
