T = int(input())  # Read the number of test cases

results = []  # Store the results for each test case

for _ in range(T):
    N = int(input())  # Read the size of the grid (N x N)
    grid = [list(input().strip()) for _ in range(N)]  # Read the grid

    east_sight_cells = 0  # Count the number of empty cells on the East side
    for row in grid:
        if row[-1] == '.' and all(cell == '.' or cell == '#' for cell in row):
            east_sight_cells += 1

    results.append(east_sight_cells)  # Store the result for this test case

print(*results, sep='\n')  # Print the results for each test case
