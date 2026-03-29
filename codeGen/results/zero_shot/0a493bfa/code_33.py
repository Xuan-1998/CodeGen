import heapq

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def f(s):
    p = 2
    while s >= p and p in [x for x in range(2, int(s ** 0.5) + 1)]:
        if p not in bad_primes:
            return f(s // p) + s
        p += 1
    return 0

n, m = map(int, input().split())
a = list(map(int, input().split()))
bad_primes = set(map(int, input().split()))

max_beauty = 0
for num in a:
    beauty = f(num)
    max_beauty = max(max_beauty, beauty)

print(max_beauty)
