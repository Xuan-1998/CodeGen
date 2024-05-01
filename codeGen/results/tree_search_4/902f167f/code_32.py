import sys

def dp(i, j, memo):
    if i <= 1 or j <= 1:
        return 0
    if (i, j) in memo:
        return memo[(i, j)]
    for k in range(1, min(i, j) + 1):
        if i % k == 0 and j % k == 0:
            result = 1 + dp(i // k, j // k, memo)
            memo[(i, j)] = result
            return result
    memo[(i, j)] = 0
    return 0

def solve(n, m):
    memo = {}
    return dp(n, m, memo)

n, m = map(int, sys.stdin.readline().split())
print(solve(n, m))
