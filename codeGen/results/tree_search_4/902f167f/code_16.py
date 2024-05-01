from functools import lru_cache

@lru_cache(maxsize=None)
def min_squares(i, j):
    if i == 0 or j == 0:
        return 0
    dp = {}
    for k in range(1, min(i, j) + 1):
        dp[(i-k, j-((i-k)%k))] = min(dp.get((i-k, j-((i-k)%k)), float('inf')), min_squares(*dp.get((i-k, j-((i-k)%k)), (0, 0))) + 1)
    return min(dp.values(), default=float('inf'))

n, m = map(int, input().split())
print(min_squares(n, m))
