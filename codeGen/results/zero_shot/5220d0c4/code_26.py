import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def min_prime_divisor(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0 and is_prime(i):
            return i

def beauty(arr, bad_primes):
    max_beauty = -float('inf')
    for num in arr:
        min_divisor = min_prime_divisor(num)
        if min_divisor not in bad_primes:
            max_beauty = max(max_beauty, min_divisor)
    return max_beauty

n, m = map(int, input().split())
arr = list(map(int, input().split()))
bad_primes = list(map(int, input().split()))

print(beauty(arr, bad_primes))
