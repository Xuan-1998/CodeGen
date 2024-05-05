def mirror_placements(grid):
    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == '.' and (i == 0 or all(grid[k][j] != '#' for k in range(i))):
                count += 1
    return count

T = int(input())
for _ in range(T):
    N = int(input())
    grid = [list(input()) for _ in range(N)]
    print(mirror_placements(grid))
