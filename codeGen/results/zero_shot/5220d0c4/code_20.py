import math

def min_prime_divisor(n):
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            return i
    return n

def beauty(num, bad_primes):
    if num in bad_primes:
        return 0
    return min_prime_divisor(num)

def total_beauty(array, bad_primes):
    return sum(beauty(num, bad_primes) for num in array)

def max_beauty(array, bad_primes):
    max_total_beauty = 0
    for r in range(len(array) + 1):
        for subset in itertools.combinations(array, r):
            total_beauty = total_beauty(subset, bad_primes)
            if total_beauty > max_total_beauty:
                max_total_beauty = total_beauty
    return max_total_beauty

n, m = map(int, input().split())
array = list(map(int, input().split()))
bad_primes = list(map(int, input().split()))

print(max_beauty(array, bad_primes))
