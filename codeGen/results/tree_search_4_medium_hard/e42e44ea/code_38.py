def min_initial_points(N, M, grid):
    dp = [[0] * N for _ in range(M)]

    # Initialize the first row and column
    for j in range(N):
        dp[0][j] = grid[0][j]
    for i in range(M):
        dp[i][0] = grid[i][0]

    # Fill up the rest of the DP table
    for i in range(1, M):
        for j in range(1, N):
            if grid[i][j] > 0:
                dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
            else:
                # If the current cell has negative points, we can't move through it
                dp[i][j] = float('inf')

    return dp[M-1][N-1]

# Example usage:
N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(M)]

print(min_initial_points(N, M, grid))
