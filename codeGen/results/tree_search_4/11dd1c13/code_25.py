def minFallingPathSum(grid):
    n = len(grid)
    dp = [[float('inf')] * n for _ in range(n)]
    dp[0] = grid[0]
    for i in range(1, n):
        prev_max_col = max(0, dp[i-1].index(min(dp[i-1])) - 1)
        for j in range(n):
            if j == 0 or j == n-1:
                dp[i][j] = dp[i-1][prev_max_col] + grid[i][j]
            else:
                dp[i][j] = min(dp[i-1][max(0, j-grid[i-1][j]) : min(n, j+grid[i-1].index(min(dp[i-1])) - 1)] + [grid[i][j]], key=sum)
    return min(dp[-1])
