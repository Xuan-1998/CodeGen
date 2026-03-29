import sys

def count_visible_cells(grid):
    N = len(grid)
    dp = [[False for _ in range(N)] for _ in range(N)]

    # Initialize dp table with False values for all cells.
    for row in range(N):
        for col in range(N):
            if grid[row][col] == '.':
                dp[row][col] = True
            elif grid[row][col] == '#':
                dp[row][col] = False

    # Update dp table based on East side visibility.
    for row in range(N-1, -1, -1):
        for col in range(N-1, -1, -1):
            if grid[row][col] == '.' and (col == N-1 or grid[row][col+1] == '#'):
                dp[row][col] = True
            elif grid[row][col] == '#':
                dp[row][col] = False

    # Count the number of empty cells with clear East side visibility.
    count = 0
    for row in range(N):
        for col in range(N):
            if dp[row][col]:
                count += 1

    return count

# Read input from stdin and print output to stdout.
T = int(sys.stdin.readline())
for _ in range(T):
    N = int(sys.stdin.readline())
    grid = [list(sys.stdin.readline().strip()) for _ in range(N)]
    print(count_visible_cells(grid))
