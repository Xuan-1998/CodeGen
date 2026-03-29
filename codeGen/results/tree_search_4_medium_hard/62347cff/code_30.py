def minPathSum(grid):
    m = len(grid)
    n = len(grid[0])
    dp = [[0 for _ in range(n)] for _ in range(m)]

    # Fill base case values (top or left boundary)
    for i in range(m):
        dp[i][0] = 0
    for j in range(n):
        dp[0][j] = 0

    # Iterate through each cell from top to bottom and left to right
    for i in range(1, m):
        for j in range(1, n):
            # Choose the minimum sum of coming from above or left
            dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]

    return dp[m-1][n-1]
