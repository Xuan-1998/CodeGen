import sys

n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

# Preprocess bad prime numbers
bad_primes = {x: i for i, x in enumerate(b)}

def gcd(x, y):
    while y:
        x, y = y, x % y
    return x

def f(s):
    p = min((p for p in range(2, int(s**0.5) + 1) if s % p == 0), default=None)
    if p and p not in bad_primes:
        return f(s // p) + s
    else:
        return f(s // p) - s

max_beauty = 0
for i in range(n):
    for j in range(i+1, n):
        k = len(set([a[i], a[j]]))
        while k > 1:
            g = gcd(a[i], a[j])
            if g > 1:
                a[i] //= g
                a[j] //= g
                k = len(set([a[i], a[j]]))
            else:
                break

max_beauty = f(sum(a))

print(max_beauty)
