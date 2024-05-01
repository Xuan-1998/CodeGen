import sys

n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

dp = [[0]*n for _ in range(n)]

for i in range(1, n):
    for j in range(1, n):
        dp[i][j] = min(dp[i-1][j], dp[i-1][j-1], dp[i][j-1]) + grid[i][j]

print(min(dp[n-1]))
