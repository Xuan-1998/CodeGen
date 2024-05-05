import sys

# Read the input
T = int(input())
for _ in range(T):
    N = int(input())
    grid = [list(input().strip()) for _ in range(N)]

    # Initialize the memoization dictionary
    memo = {}

    def f(i, j):
        if (i, j) in memo:
            return memo[(i, j)]
        
        if i == N - 1:
            return True
        
        if grid[i][j] == '#':
            return False

        # If the current cell is empty and there are no rocks to its East
        if f(i, j + 1):
            return True
        
        # If none of the above conditions are met
        memo[(i, j)] = False
        return False

    result = sum(1 for i in range(N) if f(i, 0))
    print(result)
