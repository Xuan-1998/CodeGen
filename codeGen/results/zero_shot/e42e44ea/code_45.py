M, N = map(int, input().split())
grid = []
for _ in range(M):
    grid.append(list(map(int, input().split())))

dp = [[float('inf')] * N for _ in range(M)]
dp[0][0] = 0

for i in range(M):
    for j in range(N):
        if grid[i][j] > 0:
            if i < M - 1:
                dp[i + 1][j] = min(dp[i + 1][j], dp[i][j] + grid[i][j])
            if j < N - 1:
                dp[i][j + 1] = min(dp[i][j + 1], dp[i][j] + grid[i][j])

print(dp[-1][-1])
