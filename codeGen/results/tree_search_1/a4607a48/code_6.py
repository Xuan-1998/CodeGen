from collections import deque
import sys

# Read input from stdin
n, m = map(int, sys.stdin.readline().split())
universe = [list(sys.stdin.readline().strip()) for _ in range(n)]

# Function to check if a cell is within the grid and empty
def is_valid(x, y):
    return 0 <= x < n and 0 <= y < m and universe[x][y] == '.'

# Function to calculate the shortest path between two cells using BFS
def bfs(src_x, src_y):
    queue = deque([(src_x, src_y, 0)])  # (x, y, distance)
    visited = set()
    visited.add((src_x, src_y))
    total_distance = 0
    count = 0

    while queue:
        x, y, dist = queue.popleft()
        # Process all valid neighbors
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if is_valid(nx, ny) and (nx, ny) not in visited:
                visited.add((nx, ny))
                queue.append((nx, ny, dist + 1))
                total_distance += dist + 1
                count += 1
    return total_distance, count

# Main computation to find the average lifespan
total_lifespan = 0
empty_cells = 0

for i in range(n):
    for j in range(m):
        if universe[i][j] == '.':
            distance, count = bfs(i, j)
            total_lifespan += distance
            empty_cells += count

# Calculate and print the average lifespan with 6 decimal places
average_lifespan = total_lifespan / empty_cells if empty_cells else 0
print("{:.6f}".format(average_lifespan))
