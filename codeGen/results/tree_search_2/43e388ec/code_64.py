from functools import lru_cache

@lru_cache(maxsize=None)
def solve(i, a, b):
    if i == 0:
        return (a << b) % ((10**9 + 7))
    else:
        return (2 * solve(i-1, a<<1, b)) % ((10**9 + 7))

n, m = map(int, input().split())
a, b = bin(n)[2:], bin(m)[2:]

ans = sum(solve(i, int(a), int(b)) for i in range(len(a)+len(b)))
print(ans % (10**9 + 7))
