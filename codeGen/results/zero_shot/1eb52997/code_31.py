import sys

def count_visible_cells(grid):
    visible_cells = 0
    for row in grid:
        for cell in row:
            if cell == '.' and not any(rock == '#' for rock in row[row.index(cell)+1:]):
                visible_cells += 1
    return visible_cells

T = int(sys.stdin.readline())
for _ in range(T):
    N = int(sys.stdin.readline())
    grid = [list(sys.stdin.readline().strip()) for _ in range(N)]
    print(count_visible_cells(grid))
