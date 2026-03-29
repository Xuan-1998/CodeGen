import sys

def count_mirrors(grid):
    N = len(grid)
    count = 0
    for i in range(N):
        for j in range(N - i - 1):  # Check cells to right
            if grid[i][j] == '.':
                count += 1
    return count

T = int(input())
for _ in range(T):
    N = int(input())
    grid = [input() for _ in range(N)]
    print(count_mirrors(grid))
