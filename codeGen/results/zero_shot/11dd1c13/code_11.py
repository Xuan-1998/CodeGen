grid = [[int(x) for x in input().split()] for _ in range(int(input()))]
dp = [[0]*len(grid[0]) for _ in range(len(grid))]

for i in range(1, len(grid)):
    dp[i][0] = grid[i][0] + min(dp[i-1][j] for j in range(len(grid[0])) if j != 0)
    for j in range(1, len(grid[0])):
        dp[i][j] = grid[i][j] + min((dp[i-1][k] or k==0) for k in range(len(grid[0])) if k!=j)

print(min(dp[-1]))
