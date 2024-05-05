import sys
n, m = map(int, input().split())
grid = [[int(x) for x in input().split()] for _ in range(n)]
dp = [[0]*m for _ in range(n)]

for i in range(n):
    dp[i][0] = grid[i][0]
for j in range(m):
    dp[0][j] = grid[0][j]

for i in range(1, n):
    for j in range(1, m):
        if grid[i][j] > 0:
            dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
