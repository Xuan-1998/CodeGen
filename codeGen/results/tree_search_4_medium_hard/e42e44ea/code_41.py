def min_points_required(N, M, grid):
    if N == 0 or M == 0:
        return -1

    dp = [[float('inf')] * M for _ in range(N)]

    dp[0][0] = grid[0][0]
    for i in range(1, N):
        dp[i][0] = float('inf')
    for j in range(1, M):
        dp[0][j] = float('inf')

    for i in range(1, N):
        for j in range(1, M):
            if grid[i][j] > 0:
                dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]

    return dp[N-1][M-1]
