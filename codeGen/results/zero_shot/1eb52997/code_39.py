import sys

def count_mirror_positions(n):
    # Initialize the count of mirror positions to 0
    count = 0
    
    # Iterate through each cell in the grid
    for i in range(n):
        for j in range(n):
            # Check if the current cell is an empty cell
            if grid[i][j] == '.':
                # Initialize a flag to indicate if we can see on the East side
                can_see_east = True
                
                # Iterate through all cells to the east of this cell
                for k in range(j, n):
                    # If we find a rock, set the flag to False and break the loop
                    if grid[i][k] == '#':
                        can_see_east = False
                        break
                        
                # If we can see on the East side, increment the count of mirror positions
                if can_see_east:
                    count += 1
                    
    return count

# Read the input from stdin
T = int(sys.stdin.readline())
for _ in range(T):
    n = int(sys.stdin.readline())
    grid = [list(sys.stdin.readline().strip()) for _ in range(n)]
    
    # Count the mirror positions and print the result to stdout
    print(count_mirror_positions(n))
