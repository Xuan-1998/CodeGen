import math

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def is_bad_prime(p, bad_primes):
    return p in bad_primes

def maximize_beauty(n, m, arr, bad_primes):
    max_beauty = 0
    for i in range(n):
        subset_sum = sum(arr[i+1:])
        prime_divisor = next((p for p in range(2, int(math.sqrt(subset_sum)) + 1) if gcd(subset_sum, p) == p), None)
        if is_bad_prime(prime_divisor, bad_primes):
            beauty = max_beauty - arr[i]
        else:
            beauty = max_beauty + arr[i]
        max_beauty = max(max_beauty, beauty)
    return max_beauty

n, m = map(int, input().split())
arr = list(map(int, input().split()))
bad_primes = list(map(int, input().split()))

max_beauty = maximize_beauty(n, m, arr, bad_primes)
print(max_beauty)
