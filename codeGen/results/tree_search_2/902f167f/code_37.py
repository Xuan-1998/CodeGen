from functools import lru_cache

@lru_cache(None)
def min_squares(n, m):
    if n == 0:
        return m
    if m == 0:
        return n
    
    res = float('inf')
    
    for k in range(min(n, m), 0, -1):
        res = min(res, 1 + min_squares(n-k, m-k))
    
    return res

n, m = map(int, input().split())
print(min_squares(n, m))
