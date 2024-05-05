import sys

n, m = map(int, input().split())
grid = [[int(x) for x in input().split()] for _ in range(n)]

dp = [[0] * (m+1) for _ in range(n+1)]

for i in range(n+1):
    for j in range(m+1):
        if i > 0 and j > 0:
            dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i-1][j-1]
        else:
            dp[i][j] = 0

print(dp[-1][-1])
