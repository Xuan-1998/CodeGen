import sys
from functools import lru_cache

@lru_cache(maxsize=None)
def solve(a, b):
    if b == 0:
        return a ^ (a >> (len(bin(a)) - 1))
    else:
        return a ^ ((b << 1) | (solve(a, b >> 1)))

a = int(input())
b = int(input())
print(solve(0, b) % (10**9 + 7))
