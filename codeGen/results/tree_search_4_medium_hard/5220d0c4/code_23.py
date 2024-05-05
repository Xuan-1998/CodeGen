import heapq
from math import sqrt

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def get_min_prime_divisor(n):
    for p in range(2, int(sqrt(n)) + 1):
        if n % p == 0:
            return p
    return n

def is_bad_prime(p):
    # This function checks whether a prime number is bad or not.
    # You can implement your logic here. For example, you could use a set of bad primes.
    pass

def max_beauty(n, arr, bad_primes):
    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        min_prime_divisor = get_min_prime_divisor(arr[i - 1])
        is_good = not min_prime_divisor in bad_primes
        if i == 1:
            dp[i] = 1 if is_good else 0
        else:
            for j in range(i):
                if arr[j] % min_prime_divisor == 0:
                    prev_beauty = dp[j]
                    break
            else:
                prev_beauty = 0
            dp[i] = max(dp[i - 1], prev_beauty + 1 if is_good else 0)
    return dp[n]

n, m = map(int, input().split())
arr = list(map(int, input().split()))
bad_primes = list(map(int, input().split()))

print(max_beauty(n, arr, bad_primes))
