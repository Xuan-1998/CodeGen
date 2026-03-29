import sys
from functools import lru_cache

@lru_cache(maxsize=None)
def dp(i, k):
    if i < 0 or k < 0:
        return float('inf')
    if k == 0:
        return i * (i + 1) // 2
    return min(dp(i - 1, j) for j in range(k + 1))

n = int(input())
marks = list(map(int, input().split()))

ans = dp(n, max(marks))
print(ans)
