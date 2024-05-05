def minPathSum(grid):
    m, n = len(grid), len(grid[0])
    dp = [[0] * n for _ in range(m)]

    # Initialize the base cases
    for i in range(m):
        dp[i][0] = grid[i][0]
    for j in range(n):
        dp[0][j] = grid[0][j]

    # Fill the table using dynamic programming and memoization
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]

    return dp[m-1][n-1]
