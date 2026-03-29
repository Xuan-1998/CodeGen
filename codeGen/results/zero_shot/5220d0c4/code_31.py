import math

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def beauty(arr, bad_primes):
    total_beauty = 0
    for num in arr:
        min_prime_divisor = num
        while min_prime_divisor > 1 and not is_prime(min_prime_divisor):
            min_prime_divisor -= 1
        if min_prime_divisor in bad_primes:
            total_beauty -= 1
        else:
            total_beauty += 1
    return total_beauty

n, m = map(int, input().split())
arr = list(map(int, input().split()))
bad_primes = list(map(int, input().split()))

print(beauty(arr, bad_primes))
