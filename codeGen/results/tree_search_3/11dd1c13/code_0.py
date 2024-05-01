def min_falling_path_sum(grid):
    n = len(grid)
    dp = [[0] * n for _ in range(n)]

    # Base case: first row
    for j in range(n):
        dp[0][j] = grid[0][j]

    # Fill up the rest of the dp table
    for i in range(1, n):
        for j in range(n):
            if j == 0:
                dp[i][j] = min(dp[i-1][min(j+1, n-1)]) + grid[i][j]
            elif j == n-1:
                dp[i][j] = min(dp[i-1][j]) + grid[i][j]
            else:
                dp[i][j] = min(dp[i-1][j-1], dp[i-1][min(j+1, n-1)]) + grid[i][j]

    # Return the minimum sum of a falling path with non-zero shifts
    return min(dp[-1])
