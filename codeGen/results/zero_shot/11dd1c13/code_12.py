grid = [list(map(int, input().split())) for _ in range(int(input()))]
dp = [[0] * (len(grid[0]) + 1) for _ in range(len(grid) + 1)]
for i in range(1, len(dp)):
    for j in range(1, len(dp[i])):
        if j == 1:
            dp[i][j] = grid[i-1][j-1]
        else:
            dp[i][j] = min([dp[k][j-1] + grid[i-1][k] for k in range(len(grid))]) or 0
print(min(dp[-1]))
