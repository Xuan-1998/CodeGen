n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
dp = [[float('inf')] * (m + 1) for _ in range(n + 1)]

dp[0][0] = 0

for i in range(n):
    for j in range(m):
        if i > 0 and grid[i][j] > 0:
            dp[i][j] = min(dp[i-1][j], dp[i][j-1])
        if j > 0 and grid[i][j] > 0:
            dp[i][j] = min(dp[i][j], dp[i][j-1])

for i in range(n):
    for j in range(m):
        if i < n - 1 and grid[i][j] > 0:
            dp[i+1][j] = min(dp[i+1][j], dp[i][j])
        if j < m - 1 and grid[i][j] > 0:
            dp[i][j+1] = min(dp[i][j+1], dp[i][j])

print(min(dp[-1][-1], dp[-2][-1]))
