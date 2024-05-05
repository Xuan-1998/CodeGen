N, M = map(int, input().split())
grid = [[*map(int, input().split())] for _ in range(N)]

dp = [[float('inf')] * M for _ in range(N)]
dp[0][0] = grid[0][0]

for i in range(1, N):
    dp[i][0] = min(dp[i-1][0], grid[i][0])

for j in range(1, M):
    dp[0][j] = min(dp[0][j-1], grid[0][j])

for i in range(1, N):
    for j in range(1, M):
        if grid[i][j] > 0:
            dp[i][j] = min(min(dp[i-1][j], dp[i][j-1]), grid[i][j])

print(dp[N-1][M-1])
