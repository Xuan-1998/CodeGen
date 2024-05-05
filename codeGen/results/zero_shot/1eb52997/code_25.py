import sys

def count_mirror_positions(grid):
    N = len(grid)
    result = 0
    for i in range(N):
        for j in range(N):
            if grid[i][j] == '.':  # check if cell is empty
                above_empty = all(grid[k][j] == '.' for k in range(i))
                right_empty = all(grid[i][k] == '.' for k in range(j + 1, N))
                if above_empty and right_empty:
                    result += 1
    return result

T = int(sys.stdin.readline())
for _ in range(T):
    N = int(sys.stdin.readline())
    grid = [list(sys.stdin.readline().strip()) for _ in range(N)]
    print(count_mirror_positions(grid))
