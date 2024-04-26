from itertools import product
from collections import deque

# Step 1: Representation of the universe
def read_input():
    n, m = map(int, input().split())
    universe = [input().strip() for _ in range(n)]
    return n, m, universe

# Step 2: Identifying empty cells
def find_empty_cells(universe):
    empty_cells = []
    for i, row in enumerate(universe):
        for j, cell in enumerate(row):
            if cell == '.':
                empty_cells.append((i, j))
    return empty_cells

# Step 3: Calculating the shortest paths
def bfs_shortest_path(start, end, universe):
    n, m = len(universe), len(universe[0])
    queue = deque([start])
    visited = set([start])
    distance = 0
    directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
    
    while queue:
        for _ in range(len(queue)):
            current = queue.popleft()
            if current == end:
                return distance
            for dx, dy in directions:
                x, y = current[0] + dx, current[1] + dy
                if 0 <= x < n and 0 <= y < m and universe[x][y] == '.' and (x, y) not in visited:
                    visited.add((x, y))
                    queue.append((x, y))
        distance += 1
    return -1  # In case there is no path

# Step 4: Counting paths and summing distances
def calculate_lifespan(empty_cells, universe):
    total_distance = 0
    path_count = 0
    
    for start, end in product(empty_cells, repeat=2):
        if start != end:
            path_length = bfs_shortest_path(start, end, universe)
            if path_length != -1:
                total_distance += path_length
                path_count += 1
    
    return total_distance, path_count

# Step 5: Calculating the average lifespan
def main():
    n, m, universe = read_input()
    empty_cells = find_empty_cells(universe)
    total_distance, path_count = calculate_lifespan(empty_cells, universe)
    average_lifespan = total_distance / path_count if path_count else 0
    print(f"{average_lifespan:.6f}")

# Step 6: Outputting the result
if __name__ == "__main__":
    main()
