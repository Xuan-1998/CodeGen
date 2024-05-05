python
def min_points_required():
    N, M = map(int, input().split())
    grid = [[int(i) for i in input().split()] for _ in range(N)]
    
    # Create a 2D array to store the minimum points required to reach each cell
    dp = [[float('inf')] * M for _ in range(N)]
    
    # Initialize the minimum points required to reach the top-left cell as 0
    dp[0][0] = grid[0][0]
    
    # Fill up the first row
    for j in range(1, M):
        dp[0][j] = max(dp[0][j-1], grid[0][j])
    
    # Fill up the first column
    for i in range(1, N):
        dp[i][0] = max(dp[i-1][0], grid[i][0])
    
    # Fill up the rest of the grid
    for i in range(1, N):
        for j in range(1, M):
            if grid[i][j] > 0:
                dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
    
    # The minimum points required to reach the bottom-right cell is stored in dp[N-1][M-1]
    return dp[N-1][M-1]

print(min_points_required())
