import sys

def min_initial_points(grid):
    N, M = len(grid) - 1, len(grid[0]) - 1
    dp = [[0] * (M + 1) for _ in range(N + 1)]

    for i in range(1, N + 1):
        for j in range(1, M + 1):
            if grid[i][j] > 0:
                dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
            else:
                dp[i][j] = dp[i-1][j]

    return dp[N][M]


# Read input from stdin
N, M = map(int, input().split())
grid = [[int(x) for x in input().split()] for _ in range(N)]

# Calculate and print the minimum initial points required
print(min_initial_points(grid))
