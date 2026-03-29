import sys

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def min_prime_divisor(n):
    if n <= 1:
        return None
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0 and is_prime(i):
            return i
    return n

def beauty(n, bad_primes):
    min_divisor = min_prime_divisor(n)
    if is_prime(min_divisor) and min_divisor not in bad_primes:
        return 1
    elif is_prime(min_divisor) and min_divisor in bad_primes:
        return -1
    else:
        return 0

n, m = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
bad_primes = list(map(int, sys.stdin.readline().split()))

max_beauty = max(beauty(num, bad_primes) for num in arr)
print(max_beauty)
