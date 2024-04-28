grid = [list(map(int, input().split())) for _ in range(int(input()))]
dp = [[0] * len(grid[0]) for _ in range(len(grid))]

for i in range(1, len(grid)):
    for j in range(len(grid[i])):
        dp[i][j] = min((dp[i-1][k] + grid[i][j] for k in range(len(grid[i])) if k != j), default=float('inf'))[0]
print(min(dp[-1]))
