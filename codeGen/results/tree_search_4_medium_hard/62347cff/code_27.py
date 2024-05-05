===BEGIN CODE===
def min_path_sum(grid):
    m, n = len(grid), len(grid[0])
    
    # Initialize the dp array with inf
    dp = [[float('inf')] * n for _ in range(m)]
    
    # Base case: fill top and left boundaries
    for i in range(m):
        dp[i][0] = grid[i][0]
    for j in range(n):
        dp[0][j] = grid[0][j]
    
    # Fill the rest of the cells using dynamic programming
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
    
    return dp[m-1][n-1]

# Read input from stdin
m, n = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(m)]

print(min_path_sum(grid))
