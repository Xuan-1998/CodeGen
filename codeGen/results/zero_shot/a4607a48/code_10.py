import sys

def parse_input():
    n, m = map(int, input().split())
    universe = [input().strip() for _ in range(n)]
    return n, m, universe

def count_empty_cells(universe):
    return sum(row.count('.') for row in universe)

def calculate_shortest_path_lengths(n, m, universe):
    empty_cells = [(i, j) for i in range(n) for j in range(m) if universe[i][j] == '.']
    total_path_length = 0

    for i, (start_x, start_y) in enumerate(empty_cells):
        for end_x, end_y in empty_cells[i+1:]:
            # Since no two static particles can be in one column or row,
            # the shortest path is simply the Manhattan distance.
            path_length = abs(start_x - end_x) + abs(start_y - end_y)
            total_path_length += path_length

    return total_path_length

def main():
    n, m, universe = parse_input()
    num_empty_cells = count_empty_cells(universe)
    total_path_length = calculate_shortest_path_lengths(n, m, universe)
    
    # The number of paths is the combination of empty cells taken two at a time.
    num_paths = num_empty_cells * (num_empty_cells - 1) // 2
    average_lifespan = total_path_length / num_paths if num_paths else 0

    print(f"{average_lifespan:.6f}")

if __name__ == "__main__":
    main()
