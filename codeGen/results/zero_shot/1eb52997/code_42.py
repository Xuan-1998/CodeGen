import sys

def count_mirrors(N, grid):
    mirrors = 0
    for i in range(N-1, -1, -1):  # iterate over rows from bottom up
        for j in range(N):  # iterate over cells in each row
            if grid[i][j] == '.' and all(grid[k][j] != '#' for k in range(i+1)):  # check for empty cell and no rocks above
                mirrors += 1
    return mirrors

T = int(input())  # read number of test cases
for _ in range(T):
    N = int(input())  # read grid dimensions
    grid = [list(input().strip()) for _ in range(N)]  # read grid rows
    print(count_mirrors(N, grid))  # count and print mirrors
