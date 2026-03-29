import sys
from functools import lru_cache

n = int(input())

@lru_cache(None)
def f(k):
    if k == 0:
        return [1]
    res = []
    for i in range(2, n+1):
        if (k & 1) and i > 1:
            res.append(i)
        if i <= n // 2:
            res += f((k + i - 2) // i)
    return res

@lru_cache(None)
def g(k):
    if k == 0:
        return [1]
    res = []
    for i in range(2, n+1):
        if (k & 1) and i > 1:
            res.append(i)
        if i <= n // 2:
            res += g((k + i - 2) // i)
    return res

ans = 0
for k in range(n+1):
    for r in f(k):
        if len([i for i in g(r) if r % i != 0]) == n-1:
            ans = (ans + 1) % 998244353

print(ans)
