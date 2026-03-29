import sys
from math import sqrt

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

n, m = map(int, input().split())
arr = list(map(int, input().split()))
bad_primes = list(map(int, input().split()))

def beauty(arr):
    total_beauty = 0
    for num in arr:
        if is_prime(num):
            total_beauty += -1
        else:
            min_divisor = float('inf')
            for i in range(2, int(sqrt(num)) + 1):
                if num % i == 0:
                    min_divisor = min(min_divisor, i)
            if min_divisor in bad_primes:
                total_beauty -= 1
            else:
                total_beauty += 1
    return total_beauty

print(beauty(arr))
