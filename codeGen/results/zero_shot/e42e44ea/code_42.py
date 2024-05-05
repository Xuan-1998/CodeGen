python
def min_initial_points():
    # Read input from standard input
    N, M = map(int, input().split())
    grid = [[int(x) for x in input().split()] for _ in range(N)]
    
    # Initialize a 2D array to store the minimum initial points required to reach each cell
    dp = [[0] * M for _ in range(N)]
    
    # Fill the first row and column with their respective minimum initial points
    for i in range(N):
        if grid[i][0] > 0:
            dp[i][0] = grid[i][0]
        else:
            break
    for j in range(M):
        if grid[0][j] > 0:
            dp[0][j] = grid[0][j]
        else:
            break
    
    # Fill the rest of the 2D array using dynamic programming
    for i in range(1, N):
        for j in range(1, M):
            if grid[i][j] > 0:
                dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
            else:
                dp[i][j] = float('inf')  # If the cell has zero or negative points, it's not reachable
    
    # The minimum initial points required to reach the bottom-right cell is stored in dp[N-1][M-1]
    return dp[N-1][M-1]
