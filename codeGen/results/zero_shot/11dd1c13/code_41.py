import sys
n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
dp = [[0]*n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if i == 0:
            dp[i][j] = grid[i][j]
        else:
            dp[i][j] = min(dp[i-1][k] + grid[i][j] for k in range(n) if k != j)
print(min(min(row) for row in dp))
