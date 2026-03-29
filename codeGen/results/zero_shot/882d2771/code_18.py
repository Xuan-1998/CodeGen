import sys
from functools import lru_cache

def f(n):
    @lru_cache(None)
    def fib(k):
        if k <= 1:
            return k
        else:
            return (fib(k-1) + fib(k-2)) % (10**9 + 7)

    return fib(n-1)

t, l, r = map(int, sys.stdin.readline().split())
print((sum(ti*f(i+1) for i in range(l-1, r)) - l*f(r)) * t % (10**9 + 7))
