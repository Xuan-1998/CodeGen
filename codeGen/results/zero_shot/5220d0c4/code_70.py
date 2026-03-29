import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def min_prime_divisor(n):
    for i in range(2, n+1):
        if n % i == 0 and is_prime(i):
            return i

n, m = map(int, input().split())
arr = list(map(int, input().split()))
bad_primes = list(map(int, input().split()))

beauty = 0
for num in arr:
    if num in bad_primes:
        beauty -= min_prime_divisor(num)
    else:
        beauty += min_prime_divisor(num)

print(beauty)
