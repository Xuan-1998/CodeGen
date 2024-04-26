from collections import deque
import sys

# Read input from stdin
n, m = map(int, input().split())
grid = [input() for _ in range(n)]

# Directions for movement (up, down, left, right)
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# Function to perform BFS from a given empty cell
def bfs(start):
    queue = deque([start])
    distances = [[-1 for _ in range(m)] for _ in range(n)]
    distances[start[0]][start[1]] = 0
    while queue:
        x, y = queue.popleft()
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            # Check if the new position is within bounds and is an empty cell
            if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] == '.' and distances[nx][ny] == -1:
                distances[nx][ny] = distances[x][y] + 1
                queue.append((nx, ny))
    return distances

# Calculate the sum of distances and the number of pairs of empty cells
sum_of_distances = 0
num_of_pairs = 0
for i in range(n):
    for j in range(m):
        if grid[i][j] == '.':
            distances = bfs((i, j))
            for k in range(n):
                for l in range(m):
                    if grid[k][l] == '.' and distances[k][l] != -1:
                        sum_of_distances += distances[k][l]
                        num_of_pairs += 1

# The number of pairs is counted twice (start to end and end to start), so we divide by 2
num_of_pairs //= 2

# Calculate the average lifespan and print it
average_lifespan = sum_of_distances / num_of_pairs if num_of_pairs > 0 else 0
print(f"{average_lifespan:.6f}")
