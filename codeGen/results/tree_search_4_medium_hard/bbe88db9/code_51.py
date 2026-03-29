===BEGIN CODE===
from functools import lru_cache

n = int(input())
p = list(map(int, input().split()))
@lru_cache(None)
def dp(i, j):
    if i == n+1:
        return 0
    if i > n+1:
        return 1
    if (i-1)%2 == 0:
        return min(dp(k, p[k-1]) for k in range(1, i)) + (i != n+1)
    else:
        return max(dp(k, p[k-1]) for k in range(1, i)) + (i != n+1)

print(dp(1, 0)%1000000007)
