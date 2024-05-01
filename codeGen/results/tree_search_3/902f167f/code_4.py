from sys import stdin

def min_squares(n, m):
    memo = {}
    dp = {}

    def dfs(i, j):
        if i == 0 or j == 0:
            return 0
        if (i, j) in memo:
            return memo[(i, j)]
        min_val = float('inf')
        for k in range(min(i, j), 0, -1):
            min_val = min(min_val, dfs(max(0, i-k), max(0, j-k)) + 1)
        memo[(i, j)] = min_val
        return min_val

    return dfs(n, m)

n, m = map(int, stdin.readline().split())
print(min_squares(n, m))
