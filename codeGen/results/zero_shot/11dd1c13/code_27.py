grid = [list(map(int, input().split())) for _ in range(int(input()))]
dp = [[0] * len(grid[0]) for _ in range(len(grid))]
for i in range(len(grid)):
    dp[i][0] = grid[i][0]
    for j in range(1, len(grid[0])):
        dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + grid[i][j]
print(min([dp[-1][i] for i in range(len(grid[0]))]))
