n, m = map(int, input().split())
grid = []
for _ in range(n):
    row = list(map(int, input().split()))
    grid.append(row)

dp = [[float('inf')] * (m + 1) for _ in range(n + 1)]

for i in range(n):
    for j in range(m):
        if i == 0 and j == 0:
            dp[i][j] = 0
        elif i == 0:
            dp[i][j] = dp[i][j - 1]
        elif j == 0:
            dp[i][j] = dp[i - 1][j]
        else:
            if grid[i][j] > 0:
                move_right = dp[i][j - 1] + grid[i][j]
                move_down = dp[i - 1][j] + grid[i][j]
                dp[i][j] = min(move_right, move_down)

print(dp[n - 1][m - 1])
