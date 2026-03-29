import sys

def min_points_to_reach_bottom_right(grid):
    N, M = len(grid), len(grid[0])
    dp = [[sys.maxsize] * M for _ in range(N)]
    dp[0][0] = grid[0][0]

    for i in range(1, N):
        dp[i][0] = dp[i-1][0] + grid[i][0]
    for j in range(1, M):
        dp[0][j] = dp[0][j-1] + grid[0][j]

    for i in range(1, N):
        for j in range(1, M):
            if grid[i][j] > 0:
                dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
    return dp[N-1][M-1]

# Receive input from stdin
N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]

# Print the answer to stdout
print(min_points_to_reach_bottom_right(grid))
