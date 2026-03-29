import sys

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def beauty(arr, bad_primes):
    beauty = 0
    for num in arr:
        is_good_prime = not any(is_prime(num) and prime in bad_primes for prime in range(2, int(num ** 0.5) + 1))
        if is_prime(num):
            beauty += 1 if is_good_prime else -1
        elif num > 1:
            beauty -= 1
    return beauty

n, m = map(int, input().split())
arr = list(map(int, input().split()))
bad_primes = list(map(int, input().split()))

print(beauty(arr, bad_primes))
