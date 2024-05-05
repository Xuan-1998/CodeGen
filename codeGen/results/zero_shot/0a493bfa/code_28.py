import math

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def f(s):
    p = min((i for i in range(2, int(math.sqrt(s)) + 1) if s % i == 0), default=None)
    if p and p not in bad_primes:
        return f(s // p) + s
    else:
        return f(s // p) - s

n, m = map(int, input().split())
a = list(map(int, input().split()))
bad_primes = set(map(int, input().split()))

max_beauty = 0
for i in range(n):
    for j in range(i + 1, n):
        g = gcd(a[i], a[j])
        if g not in bad_primes:
            beauty = f(g)
            max_beauty = max(max_beauty, beauty)

print(max_beauty)
