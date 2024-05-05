import sys

def min_points_required(N, M, grid):
    dp = [[sys.maxsize for _ in range(N)] for _ in range(M)]
    
    # Fill up the first row and column
    for j in range(N):
        dp[0][j] = 0 if grid[0][j] > 0 else sys.maxsize
    for i in range(M):
        dp[i][0] = grid[i][0]
        
    # Fill up the rest of the table
    for i in range(1, M):
        for j in range(1, N):
            if grid[i][j] > 0:
                dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
    
    return dp[M-1][N-1]

# Read input
N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(M)]

print(min_points_required(N, M, grid))
