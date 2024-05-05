import sys

N, M = map(int, input().split())
grid = [[int(x) for x in input().split()] for _ in range(N)]

dp = [[0] * M for _ in range(N)]

dp[0][0] = grid[0][0]

for i in range(1, N):
    dp[i][0] = max(0, dp[i - 1][0] + grid[i][0])

for j in range(1, M):
    dp[0][j] = max(0, dp[0][j - 1] + grid[0][j])

for i in range(1, N):
    for j in range(1, M):
        if grid[i][j] > 0:
            dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]

print(dp[-1][-1])
