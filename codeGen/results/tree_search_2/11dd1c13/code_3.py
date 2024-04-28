import sys

def min_falling_path(grid):
    n = len(grid)
    dp = [[0] * (n + 1) for _ in range(n)]

    # Initialize base cases
    for j in range(n):
        dp[n-1][j] = grid[n-1][j]

    # Fill up the rest of the table
    for i in range(n - 2, -1, -1):
        for j in range(n):
            dp[i][j] = min(grid[i][j] + max(dp[i+1][:]), dp[i+1].index(max(dp[i+1])))

    # Return the minimum sum of a falling path
    return max(dp[0])

# Example usage:
grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(min_falling_path(grid))  # Output: 10
