def min_initial_points(N, M, grid):
    dp = [[0] * (M + 1) for _ in range(N + 1)]
    
    # Initialize the first row and column
    for i in range(1, N + 1):
        dp[i][0] = dp[i-1][0]
    for j in range(1, M + 1):
        dp[0][j] = dp[0][j-1]

    # Fill up the dp table
    for i in range(1, N + 1):
        for j in range(1, M + 1):
            if grid[i-1][j-1] > 0:
                dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i-1][j-1]

    return dp[N][M]

N, M = map(int, input().split())
grid = [[int(x) for x in input().split()] for _ in range(N)]
print(min_initial_points(N, M, grid))
