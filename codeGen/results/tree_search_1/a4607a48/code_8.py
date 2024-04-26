from collections import deque
import sys

# Read input from stdin
n, m = map(int, input().split())
grid = [list(input().strip()) for _ in range(n)]

# Function to perform BFS and fill the dp table with shortest paths
def bfs(start_x, start_y):
    visited = [[False] * m for _ in range(n)]
    visited[start_x][start_y] = True
    queue = deque([(start_x, start_y, 0)])
    total_distance = 0

    while queue:
        x, y, distance = queue.popleft()
        total_distance += distance

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and grid[nx][ny] == '.':
                visited[nx][ny] = True
                queue.append((nx, ny, distance + 1))

    return total_distance

# Calculate the total sum of shortest paths and the number of empty cells
total_sum_of_paths = 0
num_empty_cells = 0

for i in range(n):
    for j in range(m):
        if grid[i][j] == '.':
            num_empty_cells += 1
            total_sum_of_paths += bfs(i, j)

# Calculate the average lifespan of a dynamic particle
# Note: We divide by 2 because each path is counted twice (from A to B and from B to A)
average_lifespan = total_sum_of_paths / (num_empty_cells * (num_empty_cells - 1) / 2)

# Print the result with an accuracy of at least 6 decimal places
print(f"{average_lifespan:.6f}")
