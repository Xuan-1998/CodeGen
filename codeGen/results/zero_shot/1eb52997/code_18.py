import sys

def count_mirror_cells():
    T = int(sys.stdin.readline())
    result = {}
    
    for _ in range(T):
        N = int(sys.stdin.readline())
        grid = []
        
        for _ in range(N):
            row = list(sys.stdin.readline().strip())
            grid.append(row)
            
        mirror_cells = 0
        
        # Iterate over each cell in the grid
        for i in range(N):
            for j in range(i, N):
                if grid[i][j] == '.' and not any(grid[k][j] == '#' for k in range(i+1, N)):
                    mirror_cells += 1
                    
        result[len(grid)] = mirror_cells
        
    # Print the results
    for N, count in result.items():
        print(count)

count_mirror_cells()
