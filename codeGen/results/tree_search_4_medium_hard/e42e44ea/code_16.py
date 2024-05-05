from collections import deque

def minInitialPoints(grid):
    m, n = len(grid), len(grid[0])
    dp = [[float('inf')] * n for _ in range(m)]
    
    # Base case: Initialize the top-left cell
    if grid[0][0] > 0:
        dp[0][0] = grid[0][0]
    else:
        return -1
    
    queue = deque([(0, 0, grid[0][0])])
    while queue:
        i, j, points = queue.popleft()
        
        # If we reach the bottom-right cell, return the minimum points
        if i == m - 1 and j == n - 1:
            return points
        
        # Explore rightward movements
        if j + 1 < n and grid[i][j + 1] > 0:
            new_points = max(points, grid[i][j + 1])
            if dp[i][j + 1] > new_points:
                queue.append((i, j + 1, new_points))
                dp[i][j + 1] = new_points
        
        # Explore downward movements
        if i + 1 < m and grid[i + 1][j] > 0:
            new_points = max(points, grid[i + 1][j])
            if dp[i + 1][j] > new_points:
                queue.append((i + 1, j, new_points))
                dp[i + 1][j] = new_points
    
    return -1
