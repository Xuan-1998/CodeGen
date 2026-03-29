from functools import reduce

n, m = map(int, input().split())
arr = list(map(int, input().split()))
bad_primes = list(map(int, input().split()))

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def beauty(s):
    if s == 1:
        return 0
    p = next((p for p in range(2, int(s ** 0.5) + 1) if s % p == 0), None)
    if p not in bad_primes:
        return beauty(s // p) + s
    else:
        return beauty(s // p) - s

def max_beauty():
    return sum(beauty(gcd(arr[i], reduce(lambda x, y: gcd(x, y), arr[:i] + arr[i+1:]))) for i in range(n))

print(max_beauty())
