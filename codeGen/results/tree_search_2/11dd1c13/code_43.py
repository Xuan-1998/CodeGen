def minFallingPathSum(grid):
    n = len(grid)
    m = len(grid[0])
    
    dp = [[0] * m for _ in range(n)]
    dp[0] = grid[0]
    
    for i in range(1, n):
        row = [float('inf')] * m
        for j in range(m):
            if j == 0:
                row[j] = dp[i-1][j] + grid[i][j]
            elif j == m - 1:
                row[j] = dp[i-1][j-1] + grid[i][j]
            else:
                row[j] = min(dp[i-1][j-1], dp[i-1][j]) + grid[i][j]
        dp[i] = row
    
    return min(dp[-1])

grid = [[2,1,3],[5,8,4],[1,6,12]]
print(minFallingPathSum(grid))  # Output: 11
