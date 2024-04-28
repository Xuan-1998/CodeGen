grid = [[int(x) for x in input().split()] for _ in range(int(input()))]
dp = [[0] * len(grid[0]) for _ in range(len(grid))]
for i in range(1, len(grid)):
    for j in range(len(grid[i])):
        if j == 0:
            dp[i][j] = max(dp[i-1][j], grid[i][j])
        elif j == len(grid[i])-1:
            dp[i][j] = max(dp[i-1][len(grid[i])-2], grid[i][j])
        else:
            dp[i][j] = max(min(dp[i-1][j-1], dp[i-1][j]), grid[i][j])
print(max(dp[-1]))
