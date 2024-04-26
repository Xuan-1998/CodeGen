from collections import deque
import sys

def bfs(grid, start, n, m):
    queue = deque([start])
    visited = set([start])
    distances = {start: 0}
    while queue:
        x, y = queue.popleft()
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and (nx, ny) not in visited and grid[nx][ny] == '.':
                visited.add((nx, ny))
                queue.append((nx, ny))
                distances[(nx, ny)] = distances[(x, y)] + 1
    return distances

def calculate_average_lifespan(n, m, grid):
    total_steps = 0
    total_pairs = 0
    for i in range(n):
        for j in range(m):
            if grid[i][j] == '.':
                distances = bfs(grid, (i, j), n, m)
                total_steps += sum(distances.values())
                total_pairs += len(distances) - 1  # Subtract one to exclude the starting cell
    return total_steps / total_pairs if total_pairs > 0 else 0

# Read the input from stdin
n, m = map(int, input().split())
grid = [list(input().strip()) for _ in range(n)]

# Calculate and print the average lifespan
average_lifespan = calculate_average_lifespan(n, m, grid)
print(f"{average_lifespan:.6f}")
