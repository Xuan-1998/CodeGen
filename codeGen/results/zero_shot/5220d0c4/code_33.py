import sys

def min_prime_divisor(n):
    # Check if n is divisible by any number up to its square root
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return i
    return n

def beauty(arr, bad_primes):
    max_beauty = 0
    for num in arr:
        min_divisor = min_prime_divisor(num)
        if min_divisor not in bad_primes:
            beauty_score = num // min_divisor
        else:
            beauty_score = 0
        max_beauty = max(max_beauty, beauty_score)
    return max_beauty

n, m = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
bad_primes = list(map(int, sys.stdin.readline().split()))

max_beauty = beauty(arr, bad_primes)
print(max_beauty)
