def minFallingPathSum(grid):
    n = len(grid)
    dp = [[0] * n for _ in range(n)]

    # Initialize the first row as the grid itself
    for j in range(n):
        dp[0][j] = grid[0][j]

    for i in range(1, n):
        for j in range(n):
            if j == 0:
                dp[i][j] = min(dp[i-1][k] + grid[i][j]) for k in range(1, n)]
            elif j == n - 1:
                dp[i][j] = min(dp[i-1][k] + grid[i][j]) for k in range(n - 2, -1, -1)]
            else:
                dp[i][j] = min(dp[i-1][k] + grid[i][j]) for k in range(j - 1, j + 2)]

    return min(dp[-1])
