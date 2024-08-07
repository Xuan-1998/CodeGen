code
import sys

m, n = map(int, input().split())
grid = [[int(x) for x in row.split()] for row in sys.stdin.read().strip().split('\n')]

dp = [[0] * n for _ in range(m)]

for i in range(m):
    dp[i][0] = grid[i][0]
for j in range(n):
    dp[0][j] = grid[0][j]

for i in range(1, m):
    for j in range(1, n):
        dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]

print(dp[-1][-1])
