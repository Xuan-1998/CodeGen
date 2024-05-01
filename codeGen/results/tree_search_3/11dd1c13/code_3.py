import sys

n = int(input())
grid = [[int(x) for x in input().split()] for _ in range(n)]
dp = [[0]*n for _ in range(n)]

for i in range(1, n):
    for j in range(n):
        dp[i][j] = min(dp[i-1][k] + grid[i][j] for k in range(min(j, n-1)))
print(min(dp[-1]))
