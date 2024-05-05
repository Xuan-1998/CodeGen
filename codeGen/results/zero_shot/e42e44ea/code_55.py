import sys

def min_points_required(N, M, grid):
    dp = [[0] * (M + 1) for _ in range(N + 1)]

    # Fill the DP table
    for i in range(1, N + 1):
        for j in range(1, M + 1):
            if grid[i - 1][j - 1] > 0:  # Only move down or right through cells with positive points
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i - 1][j - 1]
            else:
                dp[i][j] = sys.maxsize

    return dp[N][M]

# Read input from stdin
N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]

# Calculate the minimum initial points required
min_points = min_points_required(N, M, grid)

# Print the result to stdout
print(min_points)
