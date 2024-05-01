import sys

n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

dp = [[0] * n for _ in range(n)]

for i in range(1, n):
    for j in range(min(i+1, n), 0, -1):
        if j == i:
            dp[i][j] = sum(grid[k][j-1] for k in range(i)) + grid[i][j]
        else:
            dp[i][j] = min(dp[i-1][k] + grid[i][j] for k in range(j) if k != j-1)

print(min(dp[-1]))
