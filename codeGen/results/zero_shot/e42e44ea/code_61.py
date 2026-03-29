def min_points(grid):
    M, N = len(grid), len(grid[0])
    dp = [[float('inf')] * N for _ in range(M)]
    
    dp[0][0] = grid[0][0]
    
    for i in range(1, M):
        dp[i][0] = max(dp[i-1][0], 0) + grid[i][0]
        
    for j in range(1, N):
        dp[0][j] = max(dp[0][j-1], 0) + grid[0][j]
        
    for i in range(1, M):
        for j in range(1, N):
            dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
            
    return dp[M-1][N-1]

# Example usage
grid = [[3, 2, -1], [4, 0, 2], [-1, 3, 1]]
M, N = len(grid), len(grid[0])
print(min_points(grid))  # Output: 5

