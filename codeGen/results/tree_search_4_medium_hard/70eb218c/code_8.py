import sys
from functools import lru_cache

@lru_cache(None)
def min_ops(x, n):
    if x < 10 and n == 1:
        return 0
    if n <= 1 or len(str(x)) >= n:
        return -1
    ops = float('inf')
    for i in range(10):
        new_x = int(x * (10 ** i))
        ops = min(ops, min_ops(new_x, n - 1) + 1)
    return ops

n, x = map(int, input().split())
print(min_ops(x, n))
