from functools import lru_cache

@lru_cache(None)
def dp(i, j):
    if i == 0:
        return c[j]
    elif j > 0:
        return max(dp(i-1, k-1) + (a[i-1] if k == 0 else b[i-1]) for k in range(j+1))
    else:
        return dp(i-1, j)

n = int(input())
a = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]
c = [int(x) for x in input().split()]

print(dp(n, 0))
