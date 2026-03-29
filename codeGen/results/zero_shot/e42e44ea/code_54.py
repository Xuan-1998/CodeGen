import sys

N, M = map(int, input().split())
grid = []
for _ in range(N):
    row = list(map(int, input().split()))
    grid.append(row)

dp = [[0] * M for _ in range(N)]

# Base cases
dp[0][0] = 0
dp[N-1][M-1] = grid[N-1][M-1]

for i in range(1, N):
    dp[i][0] = dp[i-1][0] + grid[i][0]
for j in range(1, M):
    dp[0][j] = dp[0][j-1] + grid[0][j]

for i in range(1, N):
    for j in range(1, M):
        if grid[i][j] <= 0:
            dp[i][j] = dp[i-1][j] + grid[i][j]
        else:
            dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]

print(dp[N-1][M-1])
