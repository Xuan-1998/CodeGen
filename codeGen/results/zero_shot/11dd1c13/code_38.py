n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
dp = [[0]*n for _ in range(n)]

for i in range(n):
    dp[i][0] = grid[i][0]
for j in range(1, n):
    for i in range(n):
        if i == 0:
            dp[i][j] = max(dp[0][j-1], dp[0][j-2]) + grid[i][j]
        elif i == n-1:
            dp[i][j] = max(dp[i-1][j-1], dp[i-1][j-2]) + grid[i][j]
        else:
            dp[i][j] = max(max(dp[i-1][j-1], dp[i-1][j-2]), dp[i+1][j-1]) + grid[i][j]

print(min([dp[i][-1] for i in range(n)]))
