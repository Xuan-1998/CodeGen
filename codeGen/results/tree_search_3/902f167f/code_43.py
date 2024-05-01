from functools import lru_cache

@lru_cache(maxsize=None)
def min_squares(n, m):
    if n == 0 and m == 0:
        return 0
    if n > 0 and m > 0:
        return min(min_squares(n-1, m), min_squares(n, m-1)) + 1
    elif n > 0:
        return min_squares(n-1, m) + 1
    elif m > 0:
        return min_squares(n, m-1) + 1
    else:
        return 0

n, m = map(int, input().split())
print(min_squares(n, m))
