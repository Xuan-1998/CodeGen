def minFallingPathSum(grid):
    n = len(grid)
    dp = [[0] * n for _ in range(n)]

    # Initialize the first row as the grid itself
    for i in range(n):
        dp[0][i] = grid[0][i]

    for i in range(1, n):
        for j in range(n):
            min_val = float('inf')
            for k in range(n):
                if abs(k - j) != 1:  # Non-zero shift
                    min_val = min(min_val, dp[i-1][k])
            dp[i][j] = grid[i][j] + min_val

    return min(dp[-1])  # Return the minimum value of the last row
