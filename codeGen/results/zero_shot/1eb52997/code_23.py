def count_mirrors(grid):
    # Initialize the count of mirror positions to 0
    count = 0

    # Iterate over the rows and columns of the grid
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            # Check if the cell is empty (not a rock)
            if grid[i][j] == '.':
                # Check if there are no rocks to the East (right) of this cell
                east_blocked = False
                for k in range(j + 1, len(grid[i])):
                    if grid[i][k] == '#':
                        east_blocked = True
                        break

                # If there are no rocks blocking the line of sight, increment the count
                if not east_blocked:
                    count += 1

    return count

# Read input from stdin
T = int(input())
for _ in range(T):
    N = int(input())
    grid = [list(input().strip()) for _ in range(N)]

    # Calculate and print the result for each test case
    result = count_mirrors(grid)
    print(result)
