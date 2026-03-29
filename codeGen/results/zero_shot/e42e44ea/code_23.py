import sys

def min_initial_points(grid):
    M, N = len(grid), len(grid[0])
    dp = [[sys.maxsize] * N for _ in range(M)]
    dp[0][0] = 0  # top-left cell has no points initially

    for i in range(1, M):
        dp[i][0] = grid[i-1][0]
    for j in range(1, N):
        dp[0][j] = grid[0][j-1]

    for i in range(1, M):
        for j in range(1, N):
            if grid[i][j] > 0:
                dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
    return dp[-1][-1]

# Example usage
N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(M)]
print(min_initial_points(grid))
