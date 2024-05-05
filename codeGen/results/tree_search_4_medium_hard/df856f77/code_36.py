from functools import lru_cache

@lru_cache(None)
def dp(i):
    if i < 0:
        return 0
    res = float('inf')
    for j in range(i):
        if A[j] <= A[i]:
            res = min(res, dp(j) + 1)
    return res

N = int(input())
A = list(map(int, input().split()))
print(max(dp(i) for i in range(N)))
