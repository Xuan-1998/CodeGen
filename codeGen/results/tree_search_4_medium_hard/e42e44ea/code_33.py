import sys

def min_points_required(N, M, grid):
    dp = [[float('-inf')] * N for _ in range(M)]
    
    # Update base case
    dp[0][0] = 0
    
    for i in range(1, M):
        dp[i][0] = max(dp[i-1][0], 0) if grid[i][0] > 0 else float('-inf')
        
    for j in range(1, N):
        dp[0][j] = max(dp[0][j-1], 0) if grid[0][j] > 0 else float('-inf')
    
    # Fill the table
    for i in range(1, M):
        for j in range(1, N):
            if grid[i][j] > 0:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1]) + grid[i][j]
            
    return dp[M-1][N-1]

# Receive input from stdin
N, M = map(int, input().split())
grid = []
for _ in range(M):
    row = list(map(int, input().split()))
    grid.append(row)

print(min_points_required(N, M, grid))
