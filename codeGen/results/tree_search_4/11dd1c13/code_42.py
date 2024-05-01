import sys

n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

dp = [[0]*n for _ in range(n)]
for i in range(n):
    dp[i][0] = grid[i][0]
    if i > 0:
        for j in range(1, n):
            dp[i][j] = min(dp[i-1][:])
            dp[i][j] += grid[i][j]

print(min(dp[-1]))
