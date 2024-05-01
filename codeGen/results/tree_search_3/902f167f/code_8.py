import sys

def min_squares(n, m):
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    memo = {}

    def dfs(i, j):
        if (i, j) in memo:
            return memo[(i, j)]

        if i == 0 or j == 0:
            return 0

        min_squares = sys.maxsize
        for k in range(1, min(i, j) + 1):
            min_squares = min(min_squares, dfs(i - k, j) + dfs(k, m))

        memo[(i, j)] = min_squares
        return min_squares

    print(dfs(n, m))
