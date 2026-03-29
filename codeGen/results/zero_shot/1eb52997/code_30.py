T = int(input())
for _ in range(T):
    N = int(input())
    cell_state = [list(input().strip()) for _ in range(N)]
    
    east_sight_cells = 0
    for i in range(N):
        for j in range(N):
            if cell_state[i][j] == '.' and all(cell_state[k][j] != '#' for k in range(i+1, N)):
                east_sight_cells += 1
                
    print(east_sight_cells)
