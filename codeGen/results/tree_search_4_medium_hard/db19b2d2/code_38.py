code
from functools import lru_cache

@lru_cache(None)
def dp(i, k):
    if i == 0 or k == 0:
        return -1
    s = sum(1 for _ in range(m))  # calculate sum of all department sizes
    p = (s[i-1] / n) * (1 - dp(i-1, k))
    return p

n, m, h = map(int, input().split())
s = list(map(int, input().split()))
p = dp(m, n)
print(p)
