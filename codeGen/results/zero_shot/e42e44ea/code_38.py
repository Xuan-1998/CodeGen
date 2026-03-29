import sys

def min_points_to_reach_destination(N, M, grid):
    # Create a 2D array to store the minimum points needed to reach each cell
    dp = [[0] * (M + 1) for _ in range(N + 1)]

    # Fill up the first row and column of the table
    for i in range(1, N + 1):
        dp[i][0] = grid[i - 1][0]
    for j in range(1, M + 1):
        dp[0][j] = grid[0][j - 1]

    # Fill up the rest of the table
    for i in range(1, N + 1):
        for j in range(1, M + 1):
            if i > 0 and j > 0:
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i - 1][j - 1]
            elif i > 0:
                dp[i][j] = dp[i - 1][j] + grid[i - 1][j]
            else:
                dp[i][j] = dp[i][j - 1] + grid[i][j - 1]

    # Return the minimum points needed to reach the bottom-right cell
    return dp[N][M]


# Read input from stdin
N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]

# Calculate and print the result
result = min_points_to_reach_destination(N, M, grid)
print(result)
