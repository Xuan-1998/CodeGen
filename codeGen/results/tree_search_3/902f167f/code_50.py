import sys
from functools import lru_cache

@lru_cache(maxsize=None)
def dp(i, j):
    if i == 0 or j == 0:
        return 0
    min_squares = float('inf')
    for k in range(1, min(i, j) + 1):
        new_i, new_j = i - k, j - k
        min_squares = min(min_squares, dp(new_i, new_j) + (i // k) * (j // k))
    return min_squares

n, m = map(int, input().split())
print(dp(n, m))
