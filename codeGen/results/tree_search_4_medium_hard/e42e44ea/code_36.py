import sys

def min_points_to_reach(grid):
    N, M = len(grid), len(grid[0])
    dp = [[0]*M for _ in range(N)]
    
    # Initialize the first row and column with the corresponding values from the grid
    for i in range(N):
        dp[i][0] = max(0, grid[i][0])
    for j in range(M):
        dp[0][j] = max(0, grid[0][j])
    
    # Fill up the rest of the dp table using the state transition function
    for i in range(1, N):
        for j in range(1, M):
            dp[i][j] = max(dp[i-1][j], dp[i][j-1]) + grid[i][j]
    
    # Return the minimum points required to reach the bottom-right cell
    return dp[N-1][M-1]

# Read input from stdin
N, M = map(int, sys.stdin.readline().split())
grid = []
for _ in range(N):
    row = list(map(int, sys.stdin.readline().split()))
    grid.append(row)

print(min_points_to_reach(grid))
