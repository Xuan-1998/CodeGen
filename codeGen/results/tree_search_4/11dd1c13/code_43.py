def min_falling_path_sum(grid):
    m, n = len(grid), len(grid[0])
    dp = [[0] * n for _ in range(m)]

    # Initialize first row values
    for j in range(n):
        dp[0][j] = grid[0][j]

    for i in range(1, m):
        for j in range(n):
            min_sum = float('inf')
            for k in range(n):
                if k != j:  # non-zero shift
                    min_sum = min(min_sum, dp[i-1][k] + grid[i][j])
            dp[i][j] = min_sum

    return min(dp[-1])  # Return the minimum value in the last row
