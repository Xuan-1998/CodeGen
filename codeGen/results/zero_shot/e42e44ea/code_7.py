import sys
from collections import deque

def minInitialPoints(grid):
    n, m = len(grid), len(grid[0])
    
    # Create a visited grid to keep track of cells we've visited
    visited = [[False]*m for _ in range(n)]
    
    # Directions to move (right and down)
    directions = [(0, 1), (1, 0)]
    
    queue = deque([(0, 0, 0)])  # Initialize the queue with the top-left cell and 0 points
    
    while queue:
        x, y, points = queue.popleft()
        
        # If we've reached the bottom-right cell, return the minimum initial points
        if x == n-1 and y == m-1:
            return points
        
        # Explore neighbors
        for dx, dy in directions:
            nx, ny = x+dx, y+dy
            
            # Check if the neighbor is within bounds and has positive points
            if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] > 0 and not visited[nx][ny]:
                queue.append((nx, ny, points + grid[nx][ny]))
                visited[nx][ny] = True

    return -1  # If the bottom-right cell cannot be reached with positive points
