from collections import deque
import itertools

# Step 1: Read the Input
n, m = map(int, input().split())
universe = [input().strip() for _ in range(n)]

# Step 2: Find All Possible Starting and Ending Points
empty_cells = [(i, j) for i in range(n) for j in range(m) if universe[i][j] == '.']

# Step 3: Calculate All Pair Shortest Paths
def bfs(start, universe):
    visited = set()
    queue = deque([(start, 0)])
    distances = {}
    while queue:
        (x, y), dist = queue.popleft()
        if (x, y) in visited:
            continue
        visited.add((x, y))
        distances[(x, y)] = dist
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and universe[nx][ny] == '.' and (nx, ny) not in visited:
                queue.append(((nx, ny), dist + 1))
    return distances

# Calculate the shortest paths for each empty cell
all_distances = {cell: bfs(cell, universe) for cell in empty_cells}

# Step 4: Calculate the Average Lifespan
total_distance = 0
count = 0

for start, distances in all_distances.items():
    for end in empty_cells:
        if start != end:
            total_distance += distances[end]
            count += 1

average_lifespan = total_distance / count if count else 0

# Output the result
print(f"{average_lifespan:.6f}")
