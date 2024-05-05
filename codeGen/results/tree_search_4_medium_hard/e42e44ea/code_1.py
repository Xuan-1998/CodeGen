import sys

def min_points_required(grid):
    N, M = len(grid), len(grid[0])
    dp = [[0] * M for _ in range(N)]

    # Initialize first row and column
    for j in range(M):
        dp[0][j] = grid[0][j]
    for i in range(N):
        dp[i][0] = grid[i][0]

    for i in range(1, N):
        for j in range(1, M):
            if grid[i][j] > 0:
                dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    return dp[-1][-1]

# Example usage
N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]
print(min_points_required(grid))
