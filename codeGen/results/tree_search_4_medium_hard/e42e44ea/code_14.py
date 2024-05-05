import sys

N, M = map(int, input().split())
grid = []
for _ in range(N):
    row = list(map(int, input().split()))
    grid.append(row)

dp = [[0] * (M+1) for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(1, M+1):
        if grid[i-1][j-1] > 0:
            dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i-1][j-1]

print(dp[-1][-1])
