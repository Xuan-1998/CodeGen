grids = []
T = int(input())
for _ in range(T):
    N = int(input())
    grid = [list(input()) for _ in range(N)]
    grids.append(grid)

for grid in grids:
    east_visible = 0
    for i in range(N):
        for j in range(N):
            if grid[i][j] == '.' and all(grid[k][j] == '.' for k in range(i+1, N)):
                east_visible += 1
    print(east_visible)
