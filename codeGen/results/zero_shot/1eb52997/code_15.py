import sys

def count_mirror_placements(grid):
    mirror_count = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == '.':
                can_see_east = True
                for k in range(i, len(grid) - 1):
                    if grid[k + 1][j] == '#':
                        can_see_east = False
                        break
                if can_see_east:
                    mirror_count += 1
    return mirror_count

T = int(sys.stdin.readline())
for _ in range(T):
    N = int(sys.stdin.readline())
    grid = [list(sys.stdin.readline().strip()) for _ in range(N)]
    print(count_mirror_placements(grid))
