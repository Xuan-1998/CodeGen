import sys

N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]

dp = [[0] * (M) for _ in range(N)]

dp[0][0] = grid[0][0]
for i in range(1, N):
    dp[i][0] = max(dp[i-1][0], 0)
for j in range(1, M):
    dp[0][j] = max(dp[0][j-1], 0)

for i in range(1, N):
    for j in range(1, M):
        if grid[i][j] > 0:
            dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
        else:
            if dp[i-1][j] > 0:
                dp[i][j] = dp[i-1][j]
            elif dp[i][j-1] > 0:
                dp[i][j] = dp[i][j-1]
            else:
                dp[i][j] = max(dp[i-1][j], 0)
print(max(0, dp[-1][-1]))
