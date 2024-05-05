import sys

def min_initial_points(grid):
    m, n = len(grid), len(grid[0])
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if grid[i - 1][j - 1] > 0:
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i - 1][j - 1]
            else:
                dp[i][j] = dp[i - 1][j]

    return dp[m][n]

# Read input from stdin
N, M = map(int, sys.stdin.readline().split())
grid = []
for _ in range(M):
    row = list(map(int, sys.stdin.readline().split()))
    grid.append(row)

# Print the answer to stdout
print(min_initial_points(grid))
