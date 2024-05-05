def minInitialPoints(grid):
    M, N = len(grid), len(grid[0])
    dp = [[0] * N for _ in range(M)]

    # Initialize the first cell
    dp[0][0] = grid[0][0]

    # Fill in the rest of the dp table
    for i in range(1, M):
        for j in range(N):
            if j > 0:
                dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
            else:
                dp[i][j] = dp[i-1][j] + grid[i][j]

    # Return the minimum points required to reach the bottom-right cell
    return dp[-1][-1]
