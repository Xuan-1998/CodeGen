from collections import deque
import sys

def read_input():
    n, m = map(int, sys.stdin.readline().split())
    universe = [list(sys.stdin.readline().strip()) for _ in range(n)]
    return n, m, universe

def bfs_shortest_paths(universe, n, m, start):
    queue = deque([start])
    visited = set([start])
    distances = {(start[0], start[1]): 0}
    while queue:
        x, y = queue.popleft()
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and universe[nx][ny] == '.' and (nx, ny) not in visited:
                visited.add((nx, ny))
                queue.append((nx, ny))
                distances[(nx, ny)] = distances[(x, y)] + 1
    return distances

def calculate_average_lifespan(n, m, universe):
    empty_cells = [(i, j) for i in range(n) for j in range(m) if universe[i][j] == '.']
    total_distance = 0
    total_pairs = 0

    for start in empty_cells:
        distances = bfs_shortest_paths(universe, n, m, start)
        for end in distances:
            total_distance += distances[end]
            total_pairs += 1

    # Since we've counted each pair twice (start to end and end to start), divide the total pairs by 2
    average_lifespan = total_distance / (total_pairs / 2)
    return average_lifespan

def main():
    n, m, universe = read_input()
    average_lifespan = calculate_average_lifespan(n, m, universe)
    print(f"{average_lifespan:.6f}")

if __name__ == "__main__":
    main()
