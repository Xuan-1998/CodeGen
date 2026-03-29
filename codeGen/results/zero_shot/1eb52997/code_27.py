def count_mirror_positions():
    T = int(input())
    for _ in range(T):
        N = int(input())
        grid = [list(input()) for _ in range(N)]
        
        mirror_positions = 0
        for i in range(N-1): # only consider the top (N-1) rows, as we can place the mirror at most once per row
            for j in range(N):
                if grid[i][j] == '.' and grid[i+1][j] == '#': # check if there's a rock above this cell
                    mirror_positions += 1
        print(mirror_positions)

count_mirror_positions()
