import sys

def read_input():
    n, m = map(int, input().split())
    universe = [input().strip() for _ in range(n)]
    return n, m, universe

def calculate_empty_cells(universe):
    return sum(row.count('.') for row in universe)

def calculate_average_lifespan(n, m, universe):
    empty_cells = calculate_empty_cells(universe)
    total_distance = 0
    # Since the grid is guaranteed to have no static particles in the same row or column,
    # we can calculate the distance as the sum of absolute differences in x and y coordinates.
    for i in range(n):
        for j in range(m):
            if universe[i][j] == '.':
                for x in range(n):
                    for y in range(m):
                        if universe[x][y] == '.':
                            total_distance += abs(i - x) + abs(j - y)
    # The total number of paths is the number of empty cells squared minus the number of cells,
    # since we don't count the paths from a cell to itself.
    num_paths = empty_cells * (empty_cells - 1)
    average_lifespan = total_distance / num_paths if num_paths > 0 else 0
    return average_lifespan

def main():
    n, m, universe = read_input()
    average_lifespan = calculate_average_lifespan(n, m, universe)
    print(f"{average_lifespan:.6f}")

if __name__ == "__main__":
    main()
