import sys

def min_initial_points(N, M, grid):
    dp = [[0] * M for _ in range(N)]

    # Initialize boundary cases
    dp[0][j] = grid[0][j] for j in range(M)
    dp[i][0] = grid[i][0] for i in range(N)

    # Calculate minimum initial points for each cell
    for i in range(1, N):
        for j in range(1, M):
            if grid[i][j] > 0:
                dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]

    # Return the minimum initial points required to reach the bottom-right cell
    return dp[N-1][M-1]

N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]

print(min_initial_points(N, M, grid))
