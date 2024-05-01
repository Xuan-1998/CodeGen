import sys

n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

dp = [[0] * n for _ in range(n)]

for i in range(1, n):
    for j in range(1, n):
        dp[i][j] = min(dp[i-1][k] + grid[i][j] for k in range(min(j, n)))
        if i > 0 and j > 0:
            dp[i][j] = min(dp[i][j], dp[i-1][min(j-1, n-1)] + grid[i][j])

print(dp[n-1][n-1])
