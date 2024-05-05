import sys

def min_initial_points(n, m, grid):
    dp = [[0] * m for _ in range(n)]
    
    # Initialize first row and column
    dp[0][i] = grid[0][i] for i in range(m)
    for j in range(n):
        dp[j][0] = grid[j][0]
        
    # Iterate over the grid
    for i in range(1, n):
        for j in range(1, m):
            dp[i][j] = max(0, min(dp[i-1][j], dp[i][j-1])) + grid[i][j]
    
    return dp[n-1][m-1]

# Read input from stdin
n, m = map(int, sys.stdin.readline().split())
grid = []
for _ in range(n):
    row = list(map(int, sys.stdin.readline().split()))
    grid.append(row)

print(min_initial_points(n, m, grid))
