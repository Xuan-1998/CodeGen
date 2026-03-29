import sys

def count_mirrors(grid):
    mirrors = 0
    for i in range(len(grid)):
        empty_cells = 0
        rock_encountered = False
        for j in range(len(grid[i])):
            if grid[i][j] == '.':
                empty_cells += 1
            elif grid[i][j] == '#':
                rock_encountered = True
                break
        if not rock_encountered and empty_cells > 0:
            mirrors += 1
    return mirrors

T = int(sys.stdin.readline())
for _ in range(T):
    N = int(sys.stdin.readline())
    grid = [list(line.strip()) for line in sys.stdin.readlines()[:N]]
    print(count_mirrors(grid))
