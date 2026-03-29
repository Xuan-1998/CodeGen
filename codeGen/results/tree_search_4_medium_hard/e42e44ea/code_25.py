import sys

def min_points_to_reach_bottom_right(N, M, grid):
    dp = [[0] * (M) for _ in range(N)]

    # Initialize the base case
    dp[0][0] = 1 if grid[0][0] > 0 else 0

    for i in range(1, N):
        dp[i][0] = dp[i-1][0] + (1 if grid[i][0] > 0 else 0)

    for j in range(1, M):
        dp[0][j] = dp[0][j-1] + (1 if grid[0][j] > 0 else 0)

    for i in range(1, N):
        for j in range(1, M):
            if grid[i][j] > 0:
                dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + (1 if grid[i][j] > 0 else 0)

    return dp[N-1][M-1]

# Read input from stdin
N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]

# Print the minimum initial points required to reach the bottom-right cell with positive points
print(min_points_to_reach_bottom_right(N, M, grid))
