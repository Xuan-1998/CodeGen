===BEGIN CODE===
import sys
from functools import lru_cache

@lru_cache(None)
def dp(i, j):
    if i == 1:
        return 1
    if j < 0:
        return 0
    if prev_row_sum > j:
        return 1
    return sum(dp(i-1, k) for k in range(j+1))

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    prev_row_sum = sum((N-1)*[M//N] + [M%N])
    print((dp(N, M)) % 1000000000)
