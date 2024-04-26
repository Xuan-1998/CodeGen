import sys
import itertools

def read_input():
    n, m = map(int, input().split())
    grid = [input().strip() for _ in range(n)]
    return n, m, grid

def preprocess_grid(n, m, grid):
    empty_cells = []
    for i in range(n):
        for j in range(m):
            if grid[i][j] == '.':
                empty_cells.append((i, j))
    return empty_cells

def calculate_manhattan_distance(cell1, cell2):
    return abs(cell1[0] - cell2[0]) + abs(cell1[1] - cell2[1])

def calculate_average_lifespan(empty_cells):
    total_distance = 0
    pairs_count = 0

    for cell1, cell2 in itertools.combinations(empty_cells, 2):
        distance = calculate_manhattan_distance(cell1, cell2)
        total_distance += distance
        pairs_count += 1

    average_lifespan = total_distance / pairs_count if pairs_count else 0
    return average_lifespan

def main():
    n, m, grid = read_input()
    empty_cells = preprocess_grid(n, m, grid)
    average_lifespan = calculate_average_lifespan(empty_cells)
    print(f"{average_lifespan:.6f}")

if __name__ == "__main__":
    main()
