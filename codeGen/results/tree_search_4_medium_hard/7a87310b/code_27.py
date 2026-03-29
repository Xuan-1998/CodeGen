from functools import lru_cache

@lru_cache(None)
def dp(i):
    if i == 0:
        return 1
    total = 0
    for k in range(min(i+1, 3)):
        total += dp(k)
    return total

T = int(input())
for _ in range(T):
    N = int(input())
    print(dp(N))
