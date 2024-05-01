import sys

def min_falling_path(grid):
    n = len(grid)
    dp = [[0] * n for _ in range(n)]

    # Initialize first row as the same as the input grid
    dp[0] = [x for x in grid[0]]

    for i in range(1, n):
        for j in range(n):
            prev_cols = [dp[i-1][k] + grid[i][j] for k in range(n) if abs(k-j) > 0]
            dp[i][j] = min(prev_cols)

    return min(dp[-1])

# Read input from stdin
n = int(sys.stdin.readline())
grid = [list(map(int, line.split())) for _ in range(n)]

# Calculate and print the minimum sum of a falling path with non-zero shifts
print(min_falling_path(grid))
