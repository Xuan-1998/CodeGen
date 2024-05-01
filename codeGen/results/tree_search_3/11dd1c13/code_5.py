import sys

def min_falling_path_sum(grid):
    n = len(grid)
    dp = [[0] * n for _ in range(n)]

    # Initialize the first row as the grid values
    dp[0] = grid[0]

    # Fill up the DP table using the following recurrence:
    # dp[i][j] = min(dp[i-1][k]) + grid[i][j]
    # where k is not equal to j (i.e., different columns)
    for i in range(1, n):
        for j in range(n):
            if j == 0:  # leftmost column
                dp[i][j] = min(dp[i-1][k] + grid[i][j] for k in range(1, n))
            elif j == n - 1:  # rightmost column
                dp[i][j] = min(dp[i-1][k] + grid[i][j] for k in range(n-1))
            else:
                dp[i][j] = min(dp[i-1][k] + grid[i][j] for k in range(j-1, j+2))

    # The minimum sum is the smallest value in the last row
    return min(dp[-1])

# Read input from stdin and print output to stdout
grid = []
for _ in range(int(input())):
    row = list(map(int, input().split()))
    grid.append(row)

print(min_falling_path_sum(grid))
