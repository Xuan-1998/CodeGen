import sys
from functools import lru_cache

@lru_cache(maxsize=None)
def dp(n, m):
    if m == 0:
        return 1
    ans = 0
    for k in range(min(2*n+1-m, n)):
        ans += min(2*k+m, n) * dp(min(2*k+n-1, n-1), m-1)
    return ans % (10**8 + 7)

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    print(dp(n, m))
