def min_points_required(grid):
    N = len(grid)
    M = len(grid[0])
    
    dp = [[0]*M for _ in range(N)]
    
    # Fill the first row
    for i in range(M):
        if grid[0][i] > 0:
            dp[0][i] = grid[0][i]
    
    # Fill the first column
    for j in range(N):
        if grid[j][0] > 0:
            dp[j][0] = grid[j][0]
    
    # Fill the rest of the grid
    for i in range(1, N):
        for j in range(1, M):
            if grid[i][j] > 0:
                dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
    
    # The minimum points required to reach the bottom-right cell is stored at dp[N-1][M-1]
    return dp[N-1][M-1]

grid = [list(map(int, input().split())) for _ in range(int(input()))]
print(min_points_required(grid))
