import sys

T = int(sys.stdin.readline())
for _ in range(T):
    N = int(sys.stdin.readline())
    grid = []
    for _ in range(N):
        row = list(sys.stdin.readline().strip())
        grid.append(row)

    valid_spots = 0
    for i in range(N):
        for j in range(N):
            # Check if the cell is empty and if the East side (right) is not blocked by rocks
            if grid[i][j] == '.' and all(grid[k][j] == '.' for k in range(i+1, N)):
                valid_spots += 1

    print(valid_spots)
