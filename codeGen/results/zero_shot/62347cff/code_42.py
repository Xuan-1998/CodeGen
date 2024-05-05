import sys

def min_path_sum(grid):
    m, n = len(grid), len(grid[0])
    dp = [[0]*n for _ in range(m)]

    # Base cases: boundary cells
    for i in range(m):
        dp[i][0] = grid[i][0]
    for j in range(n):
        dp[0][j] = grid[0][j]

    # Fill up the dp table using the recurrence relation
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]

    # Return the minimum sum of all numbers along the path from top left to bottom right
    return dp[m-1][n-1]

# Test the function
grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(min_path_sum(grid))  # Output: 12 (path: 1+2+3+5+6+9)
