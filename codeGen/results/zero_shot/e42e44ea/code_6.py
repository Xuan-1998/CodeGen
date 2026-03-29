import sys
from collections import deque

def min_points_to_reach_destination(n, m, grid):
    # Create a queue for BFS, enqueue the top-left cell with 0 points
    queue = deque([(0, 0, 0)])  # (row, col, points)
    
    # Create a visited set to keep track of cells we've seen
    visited = set((0, 0))
    
    while queue:
        row, col, points = queue.popleft()
        
        if row == n - 1 and col == m - 1:  # Reached the destination!
            return points
        
        for dr, dc in [(-1, 0), (0, -1)]:  # Down or left
            nr, nc = row + dr, col + dc
            
            if 0 <= nr < n and 0 <= nc < m and (nr, nc) not in visited and grid[nr][nc] > 0:
                queue.append((nr, nc, points + grid[nr][nc]))
                visited.add((nr, nc))
    
    # If we reach here, it means there's no way to reach the destination
    return -1

# Read input from stdin
n, m = map(int, sys.stdin.readline().split())
grid = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

# Calculate and print the minimum points required
min_points = min_points_to_reach_destination(n, m, grid)
print(min_points)
