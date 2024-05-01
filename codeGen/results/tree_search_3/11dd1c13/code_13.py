def minFallingPathSum(grid):
    m, n = len(grid), len(grid[0])
    dp = [[float('inf')] * n for _ in range(m)]

    # Base case: The minimum sum for the first row is just the elements themselves.
    dp[0] = grid[0]

    for i in range(1, m):
        for j in range(n):
            if j == 0:
                dp[i][j] = min(dp[i-1][:])
            elif j == n - 1:
                dp[i][j] = min(dp[i-1][-1:])
            else:
                left_dp = [x for x in dp[i-1] if x != grid[i-1][j]]
                right_dp = [x for x in dp[i-1] if x != grid[i-1][n - 1 - j]]
                dp[i][j] = min(left_dp) + grid[i][j]

    return min(dp[-1])
