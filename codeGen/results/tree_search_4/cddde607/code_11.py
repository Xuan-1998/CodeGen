import sys
from collections import defaultdict

# Read input from stdin
K, N = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

# Initialize memoization table and cache
memo = defaultdict(lambda: defaultdict(int))
cache = {}

def dfs(i, j):
    if (i, j) in cache:
        return cache[(i, j)]
    
    k = arr[i][j]
    if i == N - 1 and j == N - 1:
        return 1 if k == K else 0
    
    if k > K or (i + 1 < N and j + 1 < N) and k > K:
        return 0

    dp = dfs(i - 1, j) + dfs(i, j - 1)
    
    cache[(i, j)] = dp
    return dp

# Print the result to stdout
print(dfs(0, 0))
