===BEGIN CODE===
def min_points_required(N, M, grid):
    dp = [[0] * (M) for _ in range(N)]

    # Initialize base cases
    dp[0][0] = grid[0][0]

    # Fill the first row
    for j in range(1, M):
        if grid[0][j-1] > 0:
            dp[0][j] = dp[0][j-1] + grid[0][j]
        else:
            break

    # Fill the first column
    for i in range(1, N):
        if grid[i-1][0] > 0:
            dp[i][0] = dp[i-1][0] + grid[i][0]
        else:
            break

    # Fill the rest of the grid
    for i in range(1, N):
        for j in range(1, M):
            if grid[i][j] > 0:
                dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
            else:
                break

    return dp[-1][-1]

# Read input
N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]

# Calculate the minimum points required
min_points = min_points_required(N, M, grid)

print(min_points)
