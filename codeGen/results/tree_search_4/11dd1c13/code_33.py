def minFallingPathSum(grid):
    n = len(grid)
    dp = [[0] * n for _ in range(n)]

    # Base case
    for j in range(n):
        dp[0][j] = grid[0][j]

    for i in range(1, n):
        for j in range(n):
            min_sum = float('inf')
            for k in range(n):
                if k != j:
                    min_sum = min(min_sum, dp[i-1][k]) + grid[i][j]
            dp[i][j] = min_sum

    return min(dp[-1])
