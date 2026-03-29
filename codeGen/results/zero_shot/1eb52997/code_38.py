# Read the input
T = int(input())
for _ in range(T):
    N = int(input())
    grid = []
    for _ in range(N):
        row = list(input().strip())
        grid.append(row)

    # Initialize variables
    count = 0
    for i in range(N):
        for j in range(N - 1, -1, -1): 
            if grid[i][j] == '.':
                is_visible = True
                for k in range(j + 1, N):
                    if grid[i][k] == '#':
                        break
                else:
                    count += 1

    # Print the result
    print(count)
