===BEGIN CODE===
import sys
from functools import lru_cache

@lru_cache(None)
def dp(n, k):
    if n <= 0:
        return 1.0 if k > 0 else 0.0
    if k == h:
        return 1.0
    return (dp(n-1, k) + dp(n-1, k)) / len(s)

n, m, h = map(int, input().split())
s = list(map(int, input().split()))
ans = dp(n, 0)
print(ans if ans > -1e-6 else -1)
