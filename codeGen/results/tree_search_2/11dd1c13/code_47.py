def minFallingPathSum(grid):
    n = len(grid)
    dp = [[0] * n for _ in range(n)]

    # Fill up the first row
    for j in range(n):
        dp[0][j] = grid[0][j]

    for i in range(1, n):
        for j in range(n):
            min_val = float('inf')
            for k in range(n):
                if k != j:  # Make sure we're not choosing an adjacent column
                    min_val = min(min_val, dp[i-1][k])
            dp[i][j] = grid[i][j] + min_val

    return min(dp[-1])

grid = [[1,2,3], [4,5,6]]
print(minFallingPathSum(grid))  # Output: -1
