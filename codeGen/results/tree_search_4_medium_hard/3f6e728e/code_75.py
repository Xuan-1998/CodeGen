import sys
from functools import lru_cache

@lru_cache(None)
def dfs(n, m, k):
    if n == 0 or m == 0:
        return 1
    if k > C:
        return 0
    
    res = 0
    for i in range(C+1):
        if U[n-1] == i and L[m-1] == i:
            res += dfs(n-1, m-1, k)
        elif U[n-1] >= i and L[m-1] >= i:
            res += dfs(n-1, m-1, min(U[n-1], L[m-1]) + 1)
    
    return res % (10**9+7)

T = int(input())
for _ in range(T):
    N, M, C = map(int, input().split())
    U = list(map(int, input().split()))
    L = list(map(int, input().split()))

    print(dfs(N, M, 0) % (10**9+7))
