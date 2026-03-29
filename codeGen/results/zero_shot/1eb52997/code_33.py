import sys

def count_mirrors():
    T = int(sys.stdin.readline().strip())
    for _ in range(T):
        N = int(sys.stdin.readline().strip())
        grid = [list(row.strip()) for row in (sys.stdin.readline().strip() for _ in range(N))]
        east_side_empty_cells = 0
        for row in grid:
            east_side_empty_cells += row.count('.')
        print(east_side_empty_cells)

count_mirrors()
