===BEGIN CODE===
import sys
from functools import lru_cache

@lru_cache(None)
def dp(i, j):
    if i > j:
        return 1
    res = 0
    for k in range(i, j+1):
        if M[k] == i + j // 2:
            res += (dp(i, k-1) * dp(k+1, j))
            break
    return res % (10**9 + 7)

n = int(sys.stdin.readline().strip())
M = list(map(int, sys.stdin.readline().strip().split()))
print(dp(0, n - 1))
