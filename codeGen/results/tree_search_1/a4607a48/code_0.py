from collections import deque
import sys

# Function to perform BFS and calculate shortest paths from a given cell
def bfs(grid, start, n, m, memo):
    # Directions for moving up, down, left, right
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    queue = deque([(start, 0)])  # Queue for BFS, storing (position, distance)
    visited = set()  # Set of visited positions
    visited.add(start)
    
    while queue:
        (x, y), dist = queue.popleft()
        for dx, dy in directions:
            new_x, new_y = x + dx, y + dy
            if 0 <= new_x < n and 0 <= new_y < m and grid[new_x][new_y] == '.' and (new_x, new_y) not in visited:
                visited.add((new_x, new_y))
                memo[(start, (new_x, new_y))] = dist + 1
                queue.append(((new_x, new_y), dist + 1))

# Read input from stdin
n, m = map(int, input().split())
grid = [list(input().strip()) for _ in range(n)]

# Memoization dictionary to store shortest paths
memo = {}

# Calculate shortest paths from each empty cell
for i in range(n):
    for j in range(m):
        if grid[i][j] == '.':
            bfs(grid, (i, j), n, m, memo)

# Calculate the sum of all shortest paths
total_distance = sum(memo.values())

# Calculate the number of pairs of empty cells
empty_cells = sum(row.count('.') for row in grid)
num_pairs = empty_cells * (empty_cells - 1) // 2

# Calculate the average lifespan of a dynamic particle
average_lifespan = total_distance / num_pairs
print(f"{average_lifespan:.6f}")
