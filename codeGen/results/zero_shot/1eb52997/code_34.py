import sys

def count_mirrors(grid):
    N = len(grid)
    empty_cells = 0
    for i in range(N):
        for j in range(N-1):  # Exclude the last column to ensure line of sight
            if grid[i][j] == '.' and all(grid[i][k] == '.' for k in range(j+1, N)):
                empty_cells += 1
    return empty_cells

T = int(sys.stdin.readline())
for _ in range(T):
    N = int(sys.stdin.readline())
    grid = [list(sys.stdin.readline().strip()) for _ in range(N)]
    print(count_mirrors(grid))
