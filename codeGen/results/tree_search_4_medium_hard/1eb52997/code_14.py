import sys

# Read input and store in a dictionary
T = int(input())
dp = {}
for _ in range(T):
    N = int(input())
    grid = [list(input()) for _ in range(N)]
    
    # Compute visibility states with memoization
    def compute_visibility(row, col):
        if (row, col) not in dp:
            if grid[row][col] == '.':
                dp[(row, col)] = True
            else:
                rightmost_rock_reached = False
                for c in range(col + 1, N):
                    if grid[row][c] == '#':
                        break
                    rightmost_rock_reached = True
                dp[(row, col)] = rightmost_rock_reached
        return dp[(row, col)]
    
    # Compute and print the number of possible options
    for row in range(N):
        for col in range(N):
            if compute_visibility(row, col):
                sys.stdout.write(str(1) + '\n')
                break
        else:
            sys.stdout.write('0\n')

