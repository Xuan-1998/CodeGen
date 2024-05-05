import sys

def min_points_required(N, M, grid):
    dp = [[0] * M for _ in range(N)]

    # Handle edge cases where i or j is equal to 0.
    if N > 0:
        dp[0][j] = grid[0][j]
    if M > 0:
        dp[i][0] = grid[i][0]

    for i in range(1, N):
        for j in range(1, M):
            if grid[i][j] > 0:
                dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
            else:
                # In this case, the minimum points required is negative infinity.
                # Since we're only concerned with positive points, we can set it to
                # the maximum value that Python's int type can hold.
                dp[i][j] = sys.maxsize

    return dp[N-1][M-1]

# Example usage:
N, M = map(int, input().split())
grid = []
for _ in range(N):
    row = list(map(int, input().split()))
    grid.append(row)

print(min_points_required(N, M, grid))
