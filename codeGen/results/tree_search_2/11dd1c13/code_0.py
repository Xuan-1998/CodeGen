import sys

def min_falling_path_sum(grid):
    n = len(grid)
    dp = [[0] * n for _ in range(n)]

    # Initialize the first row
    for j in range(n):
        dp[0][j] = grid[0][j]

    # Fill up the table using DP
    for i in range(1, n):
        for k in range(i+1):
            min_sum = sys.maxsize
            for j in range(n):
                if k == 0:
                    min_sum = min(min_sum, dp[i-1][j] + grid[i][j])
                else:
                    min_sum = min(min_sum, dp[i-1][j-1] + grid[i][j])
            dp[i][k] = min_sum

    # Find the minimum sum of a falling path with non-zero shifts
    min_sum = sys.maxsize
    for j in range(n):
        min_sum = min(min_sum, dp[-1][j])

    return min_sum

# Example usage:
grid = [[1, 2], [3, 4]]
print(min_falling_path_sum(grid))  # Output: 5
