def min_path_sum(grid):
    m, n = len(grid), len(grid[0])
    
    # Create a dp table with same dimensions as the grid
    dp = [[0] * n for _ in range(m)]
    
    # Initialize the top-left corner of dp table
    dp[0][0] = grid[0][0]
    
    # Fill the first column of dp table
    for i in range(1, m):
        dp[i][0] = dp[i-1][0] + grid[i][0]
    
    # Fill the first row of dp table
    for j in range(1, n):
        dp[0][j] = dp[0][j-1] + grid[0][j]
    
    # Fill the rest of the dp table
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
    
    # The minimum sum is stored at the bottom-right corner of the dp table
    return dp[-1][-1]

# Read input from standard input
m, n = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(m)]

print(min_path_sum(grid))
