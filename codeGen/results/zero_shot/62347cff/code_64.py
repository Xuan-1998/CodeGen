import sys

def min_path_sum(grid):
    m, n = len(grid), len(grid[0])
    dp = [[0] * n for _ in range(m)]

    # Initialize the base case
    dp[m-1][n-1] = grid[m-1][n-1]

    # Fill up the dp array using the recursive formula
    for i in range(m-2, -1, -1):
        for j in range(n-2, -1, -1):
            if i == m-1 and j == n-1:
                dp[i][j] = grid[i][j]
            else:
                down_sum = dp[i+1][j] + grid[i][j]
                right_sum = dp[i][j+1] + grid[i][j]
                dp[i][j] = min(down_sum, right_sum)

    # Return the minimum sum of all numbers along a path from top-left to bottom-right
    return dp[0][0]

# Example usage:
grid = [[1, 2], [3, 4]]
print(min_path_sum(grid))  # Output: 7 (path: 1 -> 2 -> 3 -> 4)
