T = int(input())
for _ in range(T):
    N = int(input())  
    grid = []  
    for _ in range(N):
        row = list(input())  
        grid.append(row)
    east_empty_cells = 0
    for i in range(N):
        for j in range(N):
            if grid[i][j] == '.' and all(grid[k][j] != '#' for k in range(i+1)):
                east_empty_cells += 1
    print(east_empty_cells)
