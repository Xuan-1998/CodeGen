def minPathSum(grid):
    m, n = len(grid), len(grid[0])
    
    # Create a dp table filled with infinity
    dp = [[float('inf')] * n for _ in range(m)]
    
    # Fill up the first row and column
    for i in range(m):
        dp[i][0] = grid[i][0]
    for j in range(n):
        dp[0][j] = grid[0][j]
    
    # Calculate the minimum path sum for each cell
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
    
    return dp[m-1][n-1]

# Read the input from stdin
m, n = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(m)]

# Calculate and print the minimum path sum
print(minPathSum(grid))
