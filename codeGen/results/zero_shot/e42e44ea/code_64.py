import sys

def min_points_to_reach_bottom_right(grid):
    N, M = len(grid), len(grid[0])
    dp = [[0] * M for _ in range(N)]

    # Initialize top-left cell
    if grid[0][0] > 0:
        dp[0][0] = grid[0][0]
    else:
        return -1  # Impossible to reach

    # Fill up the first column (downward movement)
    for i in range(1, N):
        if grid[i][0] > 0:
            dp[i][0] = dp[i-1][0] + grid[i][0]
        else:
            return -1  # Impossible to reach

    # Fill up the first row (rightward movement)
    for j in range(1, M):
        if grid[0][j] > 0:
            dp[0][j] = dp[0][j-1] + grid[0][j]
        else:
            return -1  # Impossible to reach

    # Fill up the rest of the grid
    for i in range(1, N):
        for j in range(1, M):
            if grid[i][j] > 0:
                dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
            else:
                return -1  # Impossible to reach

    # Return the minimum initial points required to reach the bottom-right cell
    return dp[-1][-1]

# Read input from stdin
N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]

# Print the output
print(min_points_to_reach_bottom_right(grid))
