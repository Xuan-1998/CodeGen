def parse_input():
    n, m = map(int, input().split())
    universe_grid = [input().strip() for _ in range(n)]
    return n, m, universe_grid

def get_empty_cells(universe_grid):
    empty_cells = []
    for i in range(len(universe_grid)):
        for j in range(len(universe_grid[i])):
            if universe_grid[i][j] == '.':
                empty_cells.append((i, j))
    return empty_cells

def calculate_average_lifespan(empty_cells):
    total_distance = 0
    num_paths = 0
    for i in range(len(empty_cells)):
        for j in range(i+1, len(empty_cells)):
            distance = abs(empty_cells[i][0] - empty_cells[j][0]) + abs(empty_cells[i][1] - empty_cells[j][1])
            total_distance += distance
            num_paths += 1
    # Since each path is counted twice, we multiply the number of paths by 2
    average_lifespan = (2 * total_distance) / (num_paths ** 2)
    return average_lifespan

# Main execution
n, m, universe_grid = parse_input()
empty_cells = get_empty_cells(universe_grid)
average_lifespan = calculate_average_lifespan(empty_cells)
print(f"{average_lifespan:.6f}")
