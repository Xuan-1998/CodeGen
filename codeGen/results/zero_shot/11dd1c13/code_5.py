import sys

n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

dp = [[0] * n for _ in range(n)]
dp[0][0] = grid[0][0]

for i in range(1, n):
    for j in range(n):
        if i == 0:
            dp[i][j] = max(dp[i][j-1], 0) + grid[i][j]
        elif j == 0:
            dp[i][j] = max(dp[i-1][j], 0) + grid[i][j]
        else:
            dp[i][j] = max(min(dp[i-1][j], dp[i][j-1]), 0) + grid[i][j]

print(min(dp[-1]))
