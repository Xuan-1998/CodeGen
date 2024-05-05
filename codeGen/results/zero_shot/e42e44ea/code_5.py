def minInitialPoints(grid):
    n, m = len(grid), len(grid[0])
    dp = [[float('inf')] * (m + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if grid[i-1][j-1] > 0:
                dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i-1][j-1]
    
    return dp[-1][-1]

# Example usage
grid = [[3,2,1,4],[5,6,3,4],[1,4,7,8]]
print(minInitialPoints(grid))  # Output: 12

