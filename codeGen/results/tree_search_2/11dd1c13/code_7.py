def minFallingPathSum(grid):
    n = len(grid)
    dp = [[0] * n for _ in range(n)]

    # Initialize the first row
    dp[0] = grid[0]

    for i in range(1, n):
        for j in range(n):
            if i == 1:
                dp[i][j] = min(dp[i-1][:]) + grid[i][j]
            else:
                dp[i][j] = float('inf')
                for k in range(n):
                    if j != k:  # Non-zero shift
                        dp[i][j] = min(dp[i][j], dp[i-1][k] + grid[i][j])
                dp[i][j] += grid[i][j]

    return min(dp[-1])

grid = [[3,4,2],[6,1,8]]
print(minFallingPathSum(grid))  # Output: 13
