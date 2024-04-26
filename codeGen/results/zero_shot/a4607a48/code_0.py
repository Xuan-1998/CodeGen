import sys
from itertools import product

# Step 1: Input Parsing
n, m = map(int, input().split())
grid = [input().strip() for _ in range(n)]

# Step 2: Grid Analysis
empty_cells = [(i, j) for i in range(n) for j in range(m) if grid[i][j] == '.']

# Step 3: Path Calculation
# Since the grid constraints guarantee that no two static particles are in one column or row
# and no diagonally adjacent cells are occupied, the shortest path is simply the Manhattan distance.
def manhattan_distance(start, end):
    return abs(start[0] - end[0]) + abs(start[1] - end[1])

# Step 4: Lifespan Calculation
total_lifespan = 0
num_paths = 0

for start, end in product(empty_cells, repeat=2):
    if start != end:
        path_length = manhattan_distance(start, end)
        total_lifespan += path_length
        num_paths += 1

# Step 5: Average Lifespan
average_lifespan = total_lifespan / num_paths

# Step 6: Output
print(f"{average_lifespan:.6f}")
