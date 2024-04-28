import sys
from functools import lru_cache

@lru_cache(maxsize=None)
def xor_shift(a, i):
    b = ((b << 1) | (a & 1)) % (10**9 + 7)
    return a ^ b

a, b = [int(x) for x in input().split()]
print(sum((xor_shift(0, i) % (10**9 + 7)) for i in range(314160)))
