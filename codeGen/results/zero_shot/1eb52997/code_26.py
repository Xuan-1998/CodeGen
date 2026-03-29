import sys

def count_empty_cells(grid):
    # Initialize counter for empty cells facing East
    east_facing_empty = 0
    
    # Iterate over each row in the grid
    for i in range(len(grid)):
        # Iterate over each cell in the current row
        for j in range(len(grid[i])):
            # Check if the current cell is empty and facing East
            if grid[i][j] == '.' and j == len(grid[i]) - 1:  # last column means facing East
                east_facing_empty += 1
    
    return east_facing_empty

def main():
    T = int(sys.stdin.readline())
    
    for _ in range(T):
        N = int(sys.stdin.readline())
        grid = [list(line.strip()) for line in sys.stdin.readlines()[:N]]
        
        print(count_empty_cells(grid))

if __name__ == "__main__":
    main()
