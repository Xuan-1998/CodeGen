def min_path_sum(grid):
    m, n = len(grid), len(grid[0])
    dp = [[0] * n for _ in range(m)]
    
    # Fill up the first row
    dp[0][j] = grid[0][j] for j in range(n)
    
    # Fill up the first column
    dp[i][0] = grid[i][0] for i in range(m)
    
    # Fill up the rest of the table
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = grid[i][j] + min(dp[i-1][j], dp[i][j-1])
    
    return dp[m-1][n-1]

# Read input from stdin
grid = [list(map(int, line.strip().split())) for line in sys.stdin.readlines()]

# Calculate and print the minimum sum of all numbers along the path from top left to bottom right
print(min_path_sum(grid))
