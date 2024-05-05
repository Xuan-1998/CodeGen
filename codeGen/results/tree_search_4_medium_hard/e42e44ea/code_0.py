from sys import stdin

def min_points(N, M, grid):
    dp = [[float('inf')] * M for _ in range(N)]

    # Base case: top-left cell (0, 0)
    if grid[0][0] > 0:
        dp[0][0] = 1
    else:
        dp[0][0] = -1

    # Fill up the first column
    for i in range(1, N):
        if grid[i][0] > 0:
            dp[i][0] = dp[i-1][0] + 1
        else:
            dp[i][0] = -float('inf')

    # Fill up the first row
    for j in range(1, M):
        if grid[0][j] > 0:
            dp[0][j] = dp[0][j-1] + 1
        else:
            dp[0][j] = -float('inf')

    # Fill up the rest of the grid
    for i in range(1, N):
        for j in range(1, M):
            if grid[i][j] > 0:
                dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + 1
            else:
                dp[i][j] = -float('inf')

    return dp[-1][-1]

# Read input from stdin
N, M = map(int, stdin.readline().split())
grid = []
for _ in range(N):
    row = list(map(int, stdin.readline().split()))
    grid.append(row)

print(min_points(N, M, grid))
