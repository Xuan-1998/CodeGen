import sys

def min_points_to_reach_bottom_right(grid):
    N, M = len(grid), len(grid[0])
    dp = [[0] * M for _ in range(N)]

    # Fill up the first row and first column
    for i in range(N):
        if grid[i][0] > 0:
            dp[i][0] = grid[i][0]
        else:
            break

    for j in range(M):
        if grid[0][j] > 0:
            dp[0][j] = grid[0][j]
        else:
            break

    # Fill up the rest of the dp table
    for i in range(1, N):
        for j in range(1, M):
            if grid[i][j] > 0:
                dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]

    # Return the minimum initial points required to reach the bottom-right cell
    return dp[-1][-1]

# Read input from stdin
N, M = map(int, sys.stdin.readline().split())
grid = [list(map(int, line.split())) for line in sys.stdin.readlines()]

# Print the result
print(min_points_to_reach_bottom_right(grid))
