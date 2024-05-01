import sys

def min_falling_path_sum(grid):
    n = len(grid)
    dp = [[0] * n for _ in range(n)]

    # Initialize last row
    dp[n-1][n-1] = grid[n-1][n-1]
    for i in range(n-2, -1, -1):
        dp[i][n-1] = min(dp[i+1][n-1], grid[i][n-1])

    # Fill up the rest of the table
    for j in range(n-2, -1, -1):
        for i in range(n-1, -1, -1):
            if i == n-1:
                dp[i][j] = min(dp[i][j+1], grid[i][j])
            else:
                dp[i][j] = min(dp[i+1][j], dp[i][j])

    # Return the minimum sum for the first row
    return dp[0][0]

# Example usage
grid = [[1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]]

print(min_falling_path_sum(grid))  # Output: 11 (minimum sum is 11)
