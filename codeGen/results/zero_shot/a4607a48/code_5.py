import itertools
import sys

def read_input():
    n, m = map(int, sys.stdin.readline().split())
    universe = [sys.stdin.readline().strip() for _ in range(n)]
    return n, m, universe

def find_empty_cells(universe):
    empty_cells = []
    for i, row in enumerate(universe):
        for j, cell in enumerate(row):
            if cell == '.':
                empty_cells.append((i, j))
    return empty_cells

def manhattan_distance(cell1, cell2):
    return abs(cell1[0] - cell2[0]) + abs(cell1[1] - cell2[1])

def calculate_average_lifespan(empty_cells):
    total_lifespan = 0
    pair_count = 0
    
    for cell1, cell2 in itertools.combinations(empty_cells, 2):
        total_lifespan += manhattan_distance(cell1, cell2)
        pair_count += 1
    
    # Since each path is counted twice (A to B and B to A), we need to double the pair count
    average_lifespan = total_lifespan / (pair_count if pair_count else 1)
    return average_lifespan

def main():
    n, m, universe = read_input()
    empty_cells = find_empty_cells(universe)
    average_lifespan = calculate_average_lifespan(empty_cells)
    print(f"{average_lifespan:.6f}")

if __name__ == "__main__":
    main()
