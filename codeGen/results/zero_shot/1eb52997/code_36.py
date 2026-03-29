import sys

def count_mirror_placements(grid):
    N = len(grid)
    count = 0
    
    # Iterate over each cell in the grid
    for i in range(N):
        for j in range(N):
            # Check if the cell is empty and there are no rocks blocking our line of sight from that cell to the East
            if grid[i][j] == '.':
                can_place_mirror = True
                
                # Check cells below this one
                for k in range(i + 1, N):
                    if grid[k][j] == '#':
                        can_place_mirror = False
                        break
                
                # If we can place the mirror at this cell, increment our count
                if can_place_mirror:
                    count += 1
    
    return count

# Read input from standard input
T = int(sys.stdin.readline())
for _ in range(T):
    N = int(sys.stdin.readline())
    grid = [list(sys.stdin.readline().strip()) for _ in range(N)]
    
    # Print the number of possible options where the mirror can be placed to see on the East side
    print(count_mirror_placements(grid))
