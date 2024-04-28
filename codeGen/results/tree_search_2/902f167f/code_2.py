import sys
from functools import lru_cache

@lru_cache(None)
def dp(i, j):
    if i == 0 or j == 0:
        return 1
    min_squares = float('inf')
    for k in range(1, min(i, j) + 1):
        temp_squares = dp(k - 1, j - 1) + (i // k) * (j // k)
        min_squares = min(min_squares, temp_squares)
    return min_squares

n, m = map(int, input().split())
print(dp(n, m))
