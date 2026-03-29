import sys
from functools import lru_cache

@lru_cache(None)
def dp(i):
    if i < 1:
        return 0.0
    if s[i-1] >= n:
        return 1.0
    return max(dp(i-1), (s[i-1]/(m-i+s[i-1])) * (1-dp(i-1)))

n, m, h = map(int, input().split())
s = list(map(int, input().split()))
if s[h-1] < n:
    print(-1.0)
else:
    print(dp(m))
