grid = [list(map(int, input().split())) for _ in range(int(input()))]
dp = [[0] * len(grid[0]) for _ in range(len(grid))]
min_sum = float('inf')
for j in range(len(grid[0])):
    dp[0][j] = grid[0][j]
    for i in range(1, len(grid)):
        min_val = min(dp[i-1])
        dp[i][j] = min_val + grid[i][j]
    min_sum = min(min_sum, dp[-1][j])

print(min_sum)
