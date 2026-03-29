import sys
from functools import lru_cache

@lru_cache(None)
def dp(i, mask):
    if i > k:
        return 1 if mask >= all_bits else 0
    res = 0
    for j in range(i-1, -1, -1):
        if (mask & (1 << j)) and (all_bits >> j) & 1:
            res += dp(j, mask ^ ((1 << j) - 1))
    return res

k, t = map(int, input().split())
for _ in range(t):
    n, k = map(int, input().split())
    all_bits = (1 << k) - 1
    print(sum(dp(i, mask) for i, mask in enumerate((all_bits >> j) & ((1 << k) - 1) for j in range(k-1, -1, -1)))) % (10**9 + 7)
