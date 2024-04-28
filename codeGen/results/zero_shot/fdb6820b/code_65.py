import sys
from functools import lru_cache

m, n = map(int, input().split())
arr = list(map(int, input().split()))

@lru_cache(None)
def dfs(i, target):
    if i == m:
        return 1 if target == 0 else 0
    if (i, target) in memo:
        return memo[(i, target)]
    
    res = 0
    for j in range(arr[i], n+1):
        res += dfs(i+1, target-j)
    memo[(i, target)] = res % (10**9 + 7)
    return memo[(i, target)]

memo = {}
print(dfs(0, n) % (10**9 + 7))
