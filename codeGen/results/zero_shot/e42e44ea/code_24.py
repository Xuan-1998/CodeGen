import sys

def find_minimum_points(N, M, grid):
    dp = [[0] * M for _ in range(N)]
    
    # Initialize the top-left cell
    dp[0][0] = grid[0][0]
    
    for i in range(1, N):
        if grid[i][0] > 0:
            dp[i][0] = dp[i-1][0] + grid[i][0]
        else:
            break
    
    for j in range(1, M):
        if grid[0][j] > 0:
            dp[0][j] = dp[0][j-1] + grid[0][j]
        else:
            break
    
    for i in range(1, N):
        for j in range(1, M):
            if grid[i][j] > 0 and (i == N-1 or j == M-1):
                dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
    
    return dp[N-1][M-1]

N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]

minimum_points = find_minimum_points(N, M, grid)
print(minimum_points)
