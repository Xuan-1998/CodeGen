def min_falling_path_sum(grid):
    m, n = len(grid), len(grid[0])
    dp = [[0] * n for _ in range(m)]

    # Base case: Initialize the first row
    for j in range(n):
        dp[0][j] = grid[0][j]

    # Fill up the rest of the dp table
    for i in range(1, m):
        for j in range(n):
            if j == 0:
                dp[i][j] = min(dp[i-1][k] for k in range(n)) + grid[i][j]
            elif j == n - 1:
                dp[i][j] = min(dp[i-1][k] for k in range(n)) + grid[i][j]
            else:
                dp[i][j] = min(min(dp[i-1][k]) + grid[i][j] for k in [j-1, j+1])

    # The minimum sum of a falling path with non-zero shifts is the smallest value in the last row
    return min(dp[-1])
