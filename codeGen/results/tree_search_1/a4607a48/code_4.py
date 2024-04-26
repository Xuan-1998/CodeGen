from collections import deque
import sys

def bfs(grid, start, n, m):
    visited = [[False for _ in range(m)] for _ in range(n)]
    queue = deque([(start, 0)])
    visited[start[0]][start[1]] = True
    total_steps = 0
    reachable_cells = 0

    while queue:
        current, steps = queue.popleft()
        total_steps += steps
        reachable_cells += 1

        for dy, dx in [(-1, 0), (1, 0), (0, -1), (0, 1)]:  # Up, down, left, right
            y, x = current[0] + dy, current[1] + dx
            if 0 <= y < n and 0 <= x < m and grid[y][x] == '.' and not visited[y][x]:
                visited[y][x] = True
                queue.append(((y, x), steps + 1))

    return total_steps, reachable_cells

def average_lifespan(grid, n, m):
    empty_cells = [(i, j) for i in range(n) for j in range(m) if grid[i][j] == '.']
    total_paths_sum = 0
    total_pairs = 0

    for cell in empty_cells:
        steps, reachable = bfs(grid, cell, n, m)
        total_paths_sum += steps
        total_pairs += reachable - 1  # Subtract 1 to exclude the starting cell

    if total_pairs == 0:
        return 0
    return total_paths_sum / total_pairs

# Read input from stdin
n, m = map(int, sys.stdin.readline().split())
grid = [list(sys.stdin.readline().strip()) for _ in range(n)]

# Calculate and print the average lifespan
average = average_lifespan(grid, n, m)
print(f"{average:.6f}")
