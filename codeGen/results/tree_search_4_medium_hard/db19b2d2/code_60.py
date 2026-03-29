===BEGIN CODE===
from functools import lru_cache

@lru_cache(None)
def dp(i, j):
    if i < 0 or j < 0:
        return 0
    if i == n and j == h:
        return (s[h] / sum(s)) if s[h] > 0 else 0
    
    p = (s[h] / sum(s)) * (i == h) if s[h] > 0 else 0
    if j < m - 1:
        return max(dp(i-1, j), dp(i, j-1)) + p
    return max(dp(i-1, j), p)

n, m, h = map(int, input().split())
s = list(map(int, input().split()))

ans = dp(n, h)
print(ans if ans > 0 else -1)
