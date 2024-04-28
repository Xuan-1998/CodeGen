import sys
from functools import lru_cache

@lru_cache(None)
def xor_left_shift(b, i):
    if i == 0:
        return b ^ (b >> 1) % (10**9 + 7)
    else:
        return xor_left_shift((b >> 1), i - 1)

a, b = map(int, input().split())
ans = sum(xor_left_shift(b, i) for i in range(315)) % (10**9 + 7)
print(ans)
