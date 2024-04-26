import sys

def read_grid(n, m):
    grid = []
    for _ in range(n):
        row = input().strip()
        grid.append(row)
    return grid

def find_empty_cells(grid, n, m):
    empty_cells = []
    for i in range(n):
        for j in range(m):
            if grid[i][j] == '.':
                empty_cells.append((i, j))
    return empty_cells

def manhattan_distance(cell1, cell2):
    return abs(cell1[0] - cell2[0]) + abs(cell1[1] - cell2[1])

def calculate_average_lifespan(empty_cells):
    total_distance = 0
    count = 0
    for i in range(len(empty_cells)):
        for j in range(i + 1, len(empty_cells)):
            total_distance += manhattan_distance(empty_cells[i], empty_cells[j])
            count += 1
    # Since we've only considered each pair once, we need to multiply by 2 for both directions
    average_lifespan = (2 * total_distance) / count if count else 0
    return average_lifespan

def main():
    n, m = map(int, input().split())
    grid = read_grid(n, m)
    empty_cells = find_empty_cells(grid, n, m)
    average_lifespan = calculate_average_lifespan(empty_cells)
    print(f"{average_lifespan:.6f}")

if __name__ == "__main__":
    main()
