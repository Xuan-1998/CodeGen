import sys

def min_initial_points(N, M, grid):
    memo = {(0, 0): grid[0][0]}  # base case: top-left cell
    for i in range(1, N):
        for j in range(M):
            if j == 0:  # only coming from above
                memo[(i, j)] = min(memo.get((i-1, j), float('inf')) + grid[i][j], sys.maxsize)
            elif i == 0:  # only coming from the left
                memo[(i, j)] = min(memo.get((i, j-1), float('inf')) + grid[i][j], sys.maxsize)
            else:
                memo[(i, j)] = min(memo.get((i-1, j), float('inf')), memo.get((i, j-1), float('inf'))) + grid[i][j]
    return memo[(N-1, M-1)]

# Read input from stdin
N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]

print(min_initial_points(N, M, grid))
