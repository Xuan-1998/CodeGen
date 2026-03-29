import math

def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

def get_prime_factors(n):
    factors = []
    for i in range(2, n + 1):
        if is_prime(i) and n % i == 0:
            factors.append(i)
    return factors

def get_k_prime_factors(k, m):
    k_prime_factors = []
    for i in range(m):
        p = next(x for x in range(2, k + 1) if is_prime(x) and k % x == 0)
        k_prime_factors.append(p)
        k //= p
    return k_prime_factors

def min_ones(n, k_prime_factors):
    ones = 0
    for p in k_prime_factors:
        if n % p == 0:
            ones += n // p - 1
    return ones

def max_distribution_index(n, k_prime_factors):
    min_ones = min_ones(n, k_prime_factors)
    return n * (n - 1) // 2 - min_ones

T = int(input())
for _ in range(T):
    n = int(input())
    m = int(input())
    k_prime_factors = get_k_prime_factors(int(input()), m)
    max_distribution_index_value = max_distribution_index(n, k_prime_factors)
    print(max_distribution_index_value % (10**9 + 7))
