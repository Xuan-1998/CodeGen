import sys

def min_points_to_reach_bottom_right(grid):
    N, M = len(grid), len(grid[0])
    dp = [[0] * M for _ in range(N)]

    # Base case: top-left cell is (0, 0)
    dp[0][0] = grid[0][0]

    # Fill up the first row
    for j in range(1, M):
        if grid[0][j] > 0:
            dp[0][j] = dp[0][j-1] + grid[0][j]
        else:
            break

    # Fill up the first column
    for i in range(1, N):
        if grid[i][0] > 0:
            dp[i][0] = dp[i-1][0] + grid[i][0]
        else:
            break

    # Fill up the rest of the grid
    for i in range(1, N):
        for j in range(1, M):
            if grid[i][j] > 0:
                dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
            else:
                break

    return dp[N-1][M-1]

# Read input from stdin
N, M = map(int, sys.stdin.readline().split())
grid = []
for _ in range(N):
    row = list(map(int, sys.stdin.readline().split()))
    grid.append(row)

# Print the answer to stdout
print(min_points_to_reach_bottom_right(grid))
