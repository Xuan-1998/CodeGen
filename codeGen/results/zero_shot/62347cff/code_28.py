def min_path_sum(grid):
    m, n = len(grid), len(grid[0])
    
    # Create a 2D DP table
    dp = [[0] * (n+1) for _ in range(m+1)]
    
    # Initialize the first row and first column of the DP table
    for j in range(n+1):
        dp[0][j] = 0
    for i in range(m+1):
        dp[i][0] = grid[i-1][0]
        
    # Fill up the DP table
    for i in range(1, m+1):
        for j in range(1, n+1):
            dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i-1][j-1]
            
    # Print the result
    print(dp[m][n])

# Test the function
grid = [[1,2,3],[5,6,9],[20,20,100]]
min_path_sum(grid)
