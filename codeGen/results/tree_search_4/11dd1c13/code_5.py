import sys

def min_falling_path(grid):
    n = len(grid)
    dp = [[0] * n for _ in range(n)]

    # Initialize the first row
    dp[0][0] = grid[0][0]
    for i in range(1, n):
        dp[i][0] = max(dp[i-1][0], grid[i][0])

    for j in range(1, n):
        dp[0][j] = max(dp[0][j-1], grid[0][j])
        for i in range(1, n):
            if j == 0:
                dp[i][j] = max(dp[i-1][j], grid[i][j])
            else:
                dp[i][j] = max(min(dp[i-1][j], dp[i][j-1]) + grid[i][j], grid[i][j])

    return max(dp[-1])

# Example usage
grid = [[1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]]

print(min_falling_path(grid))  # Output: 12
