def min_falling_path_sum(grid):
    n = len(grid)
    dp = [[0] * (n - 1) for _ in range(n)]

    # Base case: initialize dp[0][j] to 0 for all j
    for j in range(n - 1):
        dp[0][j] = grid[0][j]

    # Fill up the dp table using the refined recurrence relation
    for i in range(1, n):
        for j in range(i - 1):
            dp[i][j] = min(dp[i-1][k] + grid[i][j] for k in range(n))
        dp[i][-1] = min(dp[i-1][j] + grid[i][-1] for j in range(i))

    # Return the minimum sum of a falling path with non-zero shifts
    return min(dp[-1])

# Example usage:
grid = [[1, 2], [3, 4]]
print(min_falling_path_sum(grid))  # Output: 5 (path: 1 -> 3 -> 4)
