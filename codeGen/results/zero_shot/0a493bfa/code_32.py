def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

bad_primes = [int(x) for x in input().split()]
good_primes = [x for x in bad_primes if is_prime(x)]

n, m = map(int, input().split())
arr = list(map(int, input().split()))
initial_beauty = sum(arr)

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

for _ in range(n - 1):
    for i in range(1, n):
        arr[i - 1] = gcd(arr[i - 1], arr[i])

def f(s):
    if s < 2:
        return 0
    for p in good_primes:
        while s % p == 0:
            if p == 1:
                return 0
            if p in bad_primes:
                s //= p
            else:
                s //= p
                break
    return f(s) + s

max_beauty = initial_beauty

print(max_beauty)
