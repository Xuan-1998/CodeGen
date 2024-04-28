from functools import lru_cache

@lru_cache(None)
def dp(i, j):
    if i == 1:
        return j
    if j == 1:
        return i
    min_squares = float('inf')
    for s in range(min(i, j), 0, -1):
        k = max(0, i - s)
        if k + (j // s) <= s:
            min_squares = min(min_squares, dp(k, s) + dp(i - k, j - s))
    return min_squares

n, m = map(int, input().split())
print(dp(n, m))
