import sys

def is_prime(n):
    """Check if a number is prime"""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def beauty(num, bad_primes):
    """Calculate the beauty of a number"""
    min_prime = None
    for p in range(2, num + 1):
        if is_prime(p) and num % p == 0:
            min_prime = p
            break
    return 1 if is_prime(num) and min_prime not in bad_primes else -1

def max_beauty(arr, bad_primes):
    """Calculate the maximum beauty of the array"""
    max_b = float('-inf')
    for num in arr:
        b = beauty(num, bad_primes)
        if b > max_b:
            max_b = b
    return max_b

n, m = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
bad_primes = set(map(int, sys.stdin.readline().split()))

print(max_beauty(arr, bad_primes))
