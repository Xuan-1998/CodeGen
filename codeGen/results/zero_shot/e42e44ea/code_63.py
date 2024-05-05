from collections import deque

def min_points_required(n, m, grid):
    # Initialize queue for BFS, directions (right, down), and visited cells
    queue = deque([(0, 0, 0)])  # (row, col, points)
    visited = set((0, 0))
    
    while queue:
        row, col, points = queue.popleft()
        
        if row == n - 1 and col == m - 1:
            return points
        
        for dr, dc in [(1, 0), (0, 1)]:
            r, c = row + dr, col + dc
            
            # Check boundaries and positive points
            if 0 <= r < n and 0 <= c < m and (r, c) not in visited and grid[r][c] > 0:
                queue.append((r, c, points + grid[r][c]))
                visited.add((r, c))

n, m = map(int, input().split())
grid = []
for _ in range(n):
    row = list(map(int, input().split()))
    grid.append(row)

print(min_points_required(n, m, grid))
