n, m = map(int, input().split())
grid = [[int(x) for x in input().split()] for _ in range(n)]
dp = [[float('inf')] * (m + 1) for _ in range(n + 1)]

dp[0][0] = grid[0][0]
for i in range(n):
    for j in range(m):
        if grid[i][j] > 0:
            dp[i + 1][j + 1] = min(dp[i][j], dp[i][j + 1]) if i < n else float('inf')
            dp[i + 1][j + 1] = min(dp[i + 1][j], dp[i + 1][j + 1])
        else:
            dp[i + 1][j + 1] = float('inf')

print(min(dp[-1][-1], key=lambda x: x))
