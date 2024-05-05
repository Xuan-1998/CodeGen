from sys import stdin

N, M = map(int, stdin.readline().split())
grid = []
for _ in range(N):
    row = list(map(int, stdin.readline().split()))
    grid.append(row)

# Create dp array with same dimensions as grid
dp = [[0] * M for _ in range(N)]

dp[0][0] = grid[0][0]
for i in range(1, N):
    dp[i][0] = dp[i-1][0] + grid[i][0]
for j in range(1, M):
    dp[0][j] = dp[0][j-1] + grid[0][j]

# Fill up the rest of dp array
for i in range(1, N):
    for j in range(1, M):
        if grid[i][j] > 0:
            dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]

print(dp[-1][-1])
