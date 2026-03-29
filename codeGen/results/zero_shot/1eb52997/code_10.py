import sys

def mirror_placement_count(grid):
    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '.':
                is_clear = True
                for k in range(i+1, len(grid)):
                    if grid[k][j] == '#':
                        is_clear = False
                        break
                    if k < i and (grid[k][j] == '#' or (k + 1) % (i+1) != j):
                        is_clear = False
                        break
                if is_clear:
                    count += 1
    return count

T = int(input())
for _ in range(T):
    N = int(input())
    grid = [list(line.strip()) for line in sys.stdin.readlines()]
    print(mirror_placement_count(grid))
