from functools import lru_cache

@lru_cache(None)
def dp(i):
    if i == 0:
        return 1
    if i < 0 or not all(j <= i for j in elements):
        return 0
    
    total = 0
    for j in range(m):
        total += dp(i - elements[j])
    return total

m, N = map(int, input().split())
elements = list(map(int, input().split()))
print(dp(N) % (10**9 + 7))
