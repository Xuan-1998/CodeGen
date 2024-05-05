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

def max_beauty(n, a, bad_primes):
    beauty = 0
    for _ in range(n):
        max_gcd = 1
        for i in range(1, n):
            if i != _:
                g = gcd(a[_], a[i])
                if g > max_gcd:
                    max_gcd = g
        a[:] = [max_gcd] * (n - 1) + [a[_]]
        beauty += f(max_gcd)
    return beauty

n, m = map(int, input().split())
a = list(map(int, input().split()))
bad_primes = list(map(int, input().split()))

print(max_beauty(n, a, bad_primes))
