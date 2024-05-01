def minFallingPathSum(grid):
    m, n = len(grid), len(grid[0])
    dp = [[float('inf')] * n for _ in range(m)]
    dp[0] = grid[0]
    
    for i in range(1, m):
        for j in range(n):
            if j == 0:
                dp[i][j] = min(dp[i-1][:]) + grid[i][j]
            elif j == n-1:
                dp[i][j] = min(dp[i-1][n-1::-1]) + grid[i][j]
            else:
                dp[i][j] = min((dp[i-1][k] for k in range(n) if k != j)) + grid[i][j]
    
    return min(dp[-1])

grid = [[1,2,3], [4,5,6], [7,8,9]]
print(minFallingPathSum(grid))
