from math import gcd

def f(s):
    p = min((p for p in range(2, int(s**0.5)+1) if s % p == 0), default=s)
    if p not in bad_primes:
        return s + dp(p-1, len(a)-1)
    else:
        return s - dp(p-1, len(a)-1)

def dp(i, j):
    if i < 0 or j <= 0:
        return 0
    if memo[i][j]:
        return memo[i][j]
    res = float('-inf')
    for k in range(1, i+1):
        gcd_sum = sum(gcd(a[k-1:i], a[k-1]))
        res = max(res, dp(k-1, j-1) * f(gcd_sum))
    memo[i][j] = res
    return res

bad_primes = set()
n, m = map(int, input().split())
a = list(map(int, input().split()))
bad_primes.update(map(int, input().split()))

memo = [[float('-inf')] * (len(a)+1) for _ in range(n+1)]

max_beauty = 0
for i in range(1, n+1):
    max_beauty = max(max_beauty, dp(i, len(a)))
return max_beauty

print(max_beauty)
