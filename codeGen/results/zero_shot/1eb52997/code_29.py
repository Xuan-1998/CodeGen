import sys

def count_mirror_options(grid):
    T = int(sys.stdin.readline())
    for _ in range(T):
        N = int(sys.stdin.readline())
        grid_data = [list(sys.stdin.readline().strip()) for _ in range(N)]
        
        mirror_options = 0
        for i in range(N):
            empty_cells_to_right = 0
            for j in range(i+1, N):
                if grid_data[j][i] == '.':
                    empty_cells_to_right += 1
                else:
                    break
            mirror_options += empty_cells_to_right
        
        print(mirror_options)

count_mirror_options([])
