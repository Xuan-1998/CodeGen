def min_path_sum(grid):
    m = len(grid)
    n = len(grid[0])
    
    dp = [[0] * n for _ in range(m)]
    
    # Initialize the first row and column as 0
    dp[0][0] = grid[0][0]
    for i in range(1, m):
        dp[i][0] = dp[i-1][0] + grid[i][0]
    for j in range(1, n):
        dp[0][j] = dp[0][j-1] + grid[0][j]
    
    # Update dp[i][j] based on its neighbors (above or left)
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
    
    return dp[m-1][n-1]

# Read input from stdin
grid = []
for _ in range(int(input())):
    row = list(map(int, input().split()))
    grid.append(row)

print(min_path_sum(grid))
