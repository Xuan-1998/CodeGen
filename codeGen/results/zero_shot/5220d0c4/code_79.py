n, m = map(int, input().split())
arr = list(map(int, input().split()))
bad_primes = list(map(int, input().split()))

def generate_primes(n):
    primes = [True] * (n + 1)
    primes[0] = primes[1] = False
    p = 2
    while p * p <= n:
        if primes[p]:
            for i in range(p * p, n + 1, p):
                primes[i] = False
        p += 1
    return [p for p in range(2, n + 1) if primes[p]]

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

max_val = max(arr)
primes = generate_primes(max_val)
bad_primes = [p for p in primes if is_prime(p)]

def calculate_beauty(x):
    min_prime = None
    for p in primes:
        if x % p == 0 and (p not in bad_primes or x < p * p):
            min_prime = p
            break
    return 1 if min_prime is None else -min_prime

beauties = [calculate_beauty(x) for x in arr]

print(max(beauties))
