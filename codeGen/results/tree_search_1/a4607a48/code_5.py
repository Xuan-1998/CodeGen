from collections import deque
import sys

def bfs(grid, start, n, m):
    queue = deque([start])
    visited = [[False] * m for _ in range(n)]
    visited[start[0]][start[1]] = True
    distance = [[0] * m for _ in range(n)]
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    while queue:
        x, y = queue.popleft()
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and grid[nx][ny] == '.':
                visited[nx][ny] = True
                distance[nx][ny] = distance[x][y] + 1
                queue.append((nx, ny))
    return distance

def main():
    n, m = map(int, sys.stdin.readline().split())
    grid = [list(sys.stdin.readline().strip()) for _ in range(n)]

    total_distance = 0
    empty_cells = 0
    
    for i in range(n):
        for j in range(m):
            if grid[i][j] == '.':
                distances = bfs(grid, (i, j), n, m)
                for ii in range(n):
                    for jj in range(m):
                        if grid[ii][jj] == '.':
                            total_distance += distances[ii][jj]
                empty_cells += 1

    # Average lifespan is the total distance divided by the number of pairs of empty cells
    average_lifespan = total_distance / (empty_cells * (empty_cells - 1))
    print(f"{average_lifespan:.6f}")

if __name__ == "__main__":
    main()
