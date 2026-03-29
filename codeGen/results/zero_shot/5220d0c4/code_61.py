import sys

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def max_beauty(arr, bad_primes):
    beauty = 0
    for num in arr:
        is_good_prime = not any(num in bad_primes)
        if is_good_prime and is_prime(num):
            beauty += 1
        elif is_prime(num) and num in bad_primes:
            beauty -= 1
    return beauty

n, m = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
bad_primes = list(map(int, sys.stdin.readline().split()))

print(max_beauty(arr, bad_primes))
