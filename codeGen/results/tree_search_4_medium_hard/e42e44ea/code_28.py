from typing import List

def minInitialPoints(grid: List[List[int]]) -> int:
    m, n = len(grid), len(grid[0])
    
    dp = [[0] * n for _ in range(m)]
    
    # Base case: top-left cell has 0 initial points
    dp[0][0] = grid[0][0]
    
    for i in range(1, m):
        # For cells that are not at the top edge (i > 0)
        if grid[i][0] > 0:
            dp[i][0] = max(dp[i-1][0], -grid[i][0])
        else:
            dp[i][0] = float('inf')  # Set to infinity
    
    for j in range(1, n):
        # For cells that are not at the left edge (j > 0)
        if grid[0][j] > 0:
            dp[0][j] = max(dp[0][j-1], -grid[0][j])
        else:
            dp[0][j] = float('inf')  # Set to infinity
    
    for i in range(1, m):
        for j in range(1, n):
            if grid[i][j] > 0:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1]) - grid[i][j]
            else:
                dp[i][j] = float('inf')  # Set to infinity
    
    return min(min(row) for row in dp)
