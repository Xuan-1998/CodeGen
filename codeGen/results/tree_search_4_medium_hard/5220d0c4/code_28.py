import sys

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def filter_primes(arr):
    primes = []
    for num in arr:
        if is_prime(num):
            primes.append(num)
    return primes

def calculate_beauty(prime, bad_primes):
    if prime in bad_primes:
        return prime - 1
    return prime

def max_beauty(n, m, arr, bad_primes):
    filtered_primes = filter_primes(arr)
    beauty_values = [calculate_beauty(p, bad_primes) for p in filtered_primes]
    return max(beauty_values)

n, m = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
bad_primes = list(map(int, sys.stdin.readline().split()))

print(max_beauty(n, m, arr, bad_primes))
