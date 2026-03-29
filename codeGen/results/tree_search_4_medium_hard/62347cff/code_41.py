def minPathSum(grid):
    m = len(grid)
    n = len(grid[0])
    
    dp = [[0] * n for _ in range(m)]
    
    # Initialize the first row and column with their respective values from the top or left boundary.
    dp[0][0] = grid[0][0]
    for i in range(1, m):
        dp[i][0] = dp[i-1][0] + grid[i][0]
    for j in range(1, n):
        dp[0][j] = dp[0][j-1] + grid[0][j]
    
    # Fill up the dynamic programming table.
    for i in range(1, m):
        for j in range(1, n):
            # The state expression is the minimum of coming from above and coming from left, plus the value at the current cell.
            dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
    
    return dp[m-1][n-1]

# Read input from stdin.
grid = []
for _ in range(int(input())):
    row = list(map(int, input().split()))
    grid.append(row)

# Print the minimum sum of all numbers along the path from the top left corner to the bottom right corner of the grid.
print(minPathSum(grid))
