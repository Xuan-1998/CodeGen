import sys
import itertools

def parse_input():
    n, m = map(int, input().split())
    universe = [input().strip() for _ in range(n)]
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
    sum_of_distances = 0
    count_of_distances = 0
    for cell1, cell2 in itertools.combinations(empty_cells, 2):
        distance = manhattan_distance(cell1, cell2)
        sum_of_distances += distance
        count_of_distances += 1
    average_lifespan = sum_of_distances / count_of_distances
    return average_lifespan

def main():
    n, m, universe = parse_input()
    empty_cells = find_empty_cells(universe)
    average_lifespan = calculate_average_lifespan(empty_cells)
    print(f"{average_lifespan:.6f}")

if __name__ == "__main__":
    main()
