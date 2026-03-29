import sys

def read_input():
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    bad_primes = list(map(int, input().split()))
    return n, m, arr, bad_primes

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def find_min_divisor(n):
    for i in range(2, n+1):
        if n % i == 0 and is_prime(i):
            return i

def max_beauty(arr, bad_primes):
    beauty = 0
    for num in arr:
        min_divisor = find_min_divisor(num)
        if min_divisor not in bad_primes:
            beauty += 1
    return beauty

n, m, arr, bad_primes = read_input()
print(max_beauty(arr, bad_primes))
