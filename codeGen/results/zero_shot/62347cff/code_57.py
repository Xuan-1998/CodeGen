def min_path_sum(grid):
    m, n = len(grid), len(grid[0])
    
    # Create a 2D array to store the minimum sum of all numbers along each path
    dp = [[0] * n for _ in range(m)]
    
    # Initialize the first element as the value at the top left corner
    dp[0][0] = grid[0][0]
    
    # Fill up the first row (moving right)
    for i in range(1, n):
        dp[0][i] = dp[0][i-1] + grid[0][i]
    
    # Fill up the first column (moving down)
    for i in range(1, m):
        dp[i][0] = dp[i-1][0] + grid[i][0]
    
    # Fill up the rest of the 2D array
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
    
    return dp[m-1][n-1]

# Receive input from stdin
m, n = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(m)]

# Calculate the minimum path sum and print it to stdout
print(min_path_sum(grid))
