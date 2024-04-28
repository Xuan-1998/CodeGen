from functools import lru_cache

@lru_cache(None)
def min_squares(n, m):
    if n == 1 or m == 1:
        return max(n, m)

    return min(min_squares(n-1, m) + 1, min_squares(n, m-1) + 1)

n, m = map(int, input().split())
print(min_squares(n, m))
