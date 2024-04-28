def minSquares(n, m):
    dp = {}
    for i in range(1, n+1):
        for j in range(1, m+1):
            if i < 2 or j < 2:
                dp[(i, j)] = 1
            else:
                min_squares = float('inf')
                for k in range(1, i+1):
                    for l in range(1, j+1):
                        if k <= i and l <= j:
                            min_squares = min(min_squares, dp.get((min(i, k), min(j, l)), 0) + 1)
                dp[(i, j)] = min_squares
    return dp.get((n, m), float('inf'))

# Read input from stdin
n, m = map(int, input().split())

print(minSquares(n, m))
