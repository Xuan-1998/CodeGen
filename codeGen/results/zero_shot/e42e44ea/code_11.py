import sys

def min_points_to_reach_destination(M, N, grid):
    dp = [[0] * (N + 1) for _ in range(M + 1)]

    for i in range(1, M + 1):
        for j in range(1, N + 1):
            if grid[i-1][j-1] > 0:  # Only move down and right
                dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i-1][j-1]
            else:
                dp[i][j] = sys.maxsize  # No movement allowed in negative points

    return dp[M][N]

# Input: Read M, N and the grid from standard input
M, N = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(M)]

# Calculate the minimum points required to reach the destination
min_points = min_points_to_reach_destination(M, N, grid)

print(min_points)
