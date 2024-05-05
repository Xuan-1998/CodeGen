import sys
from collections import deque

# Read input from stdin
N, M = map(int, input().split())
grid = [[int(x) for x in input().split()] for _ in range(N)]

# Define the directions (right and down)
directions = [(0, 1), (1, 0)]

# Initialize the queue with the starting point (top-left cell)
queue = deque([(0, 0, grid[0][0])])

# Create a visited set to keep track of visited cells
visited = {(0, 0)}

# Define the minimum initial points required to reach the bottom-right cell
min_points = float('inf')

while queue:
    x, y, points = queue.popleft()
    
    # If we have reached the bottom-right cell, update min_points
    if x == N - 1 and y == M - 1:
        min_points = min(min_points, points)
        
    # Explore neighboring cells
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        
        # Check if the neighboring cell is within bounds and has positive points
        if (0 <= nx < N) and (0 <= ny < M) and (nx, ny) not in visited and grid[nx][ny] > 0:
            queue.append((nx, ny, points + grid[nx][ny]))
            visited.add((nx, ny))

# Print the minimum initial points required to reach the bottom-right cell
print(min_points)
