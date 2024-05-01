def minFallingPathSum(grid):
    n = len(grid)
    dp = [[0] * len(grid[0]) for _ in range(n+1)]

    for i in range(n+1):
        if i == 0:
            continue
        for j in range(len(grid[0])):
            if i == 1:
                dp[i][j] = grid[0][j]
            else:
                dp[i][j] = min(dp[i-1][k], grid[i][j]) + grid[i][j]

    return min(dp[-1])
