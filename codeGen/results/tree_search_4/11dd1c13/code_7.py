def min_falling_path_sum(grid):
    n = len(grid)
    m = len(grid[0])
    
    dp = [[0] * m for _ in range(n)]
    
    # Base case: The minimum sum for the first row is just the grid values
    dp[0] = grid[0]
    
    for i in range(1, n):
        for j in range(m):
            if i % 2 == 0:
                # For even rows, consider left and right shifts
                dp[i][j] = min((dp[i-1][k] + grid[i][j]) for k in range(m))
            else:
                # For odd rows, consider right and left shifts
                dp[i][j] = min((dp[i-1][m-1-k] + grid[i][j]) for k in range(m))
    
    return min(dp[-1])

# Read the input grid from standard input
grid = [list(map(int, line.split())) for line in sys.stdin.readlines()]

print(min_falling_path_sum(grid))
