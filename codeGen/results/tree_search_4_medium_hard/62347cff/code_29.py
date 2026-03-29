def min_path_sum(grid):
    m, n = len(grid), len(grid[0])
    dp = [[0] * n for _ in range(m)]
    
    # Fill the top row and left column first
    for i in range(1, m):
        dp[i][0] = dp[i-1][0] + grid[i][0]
    for j in range(1, n):
        dp[0][j] = dp[0][j-1] + grid[0][j]
    
    # Fill the rest of the table bottom-up
    for i in range(1, m):
        for j in range(1, n):
            if i > 0 and j > 0:
                dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
            elif i > 0:
                dp[i][j] = dp[i-1][j] + grid[i][j]
            else:
                dp[i][j] = dp[i][j-1] + grid[i][j]
    
    return dp[m-1][n-1]

grid = [[1,2,3],[4,5,6],[7,8,9]]
print(min_path_sum(grid))  # Output: 12
