def min_initial_points(N, M, grid):
    dp = [[0] * M for _ in range(N)]

    # Base cases
    for j in range(M):
        dp[0][j] = grid[0][j]
    for i in range(N):
        dp[i][0] = grid[i][0]

    # Fill up the dynamic programming table
    for i in range(1, N):
        for j in range(1, M):
            dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]

    # Return the minimum initial points required to reach the bottom-right cell
    return dp[-1][-1]
