import sys
from functools import lru_cache

t, l, r = map(int, input().split())
mod = 10**9 + 7

@lru_cache(None)
def f(i, j):
    if i == 1:
        return 0
    if j == 1:
        return i - 1
    return min(f(i-1, k) for k in range(2, j+1)) + i - 1

print(sum(t*i*(r-l+1)//i*f(i, r//i)) % mod)
