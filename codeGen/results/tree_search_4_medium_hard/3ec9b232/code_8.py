import sys
from functools import lru_cache

n = int(input())
m = list(map(int, input().split()))
k = m.count(1)

@lru_cache(None)
def dp(i, j):
    if i == 0:
        return 1
    elif j == 0:
        return sum(dp(i-1, x) for x in range(i)) % (10**9 + 7)
    else:
        return sum(dp(i-1, x)*dp(0, min(j-1, x)) for x in range(min(j, i))) % (10**9 + 7)

print(dp(n, k))
