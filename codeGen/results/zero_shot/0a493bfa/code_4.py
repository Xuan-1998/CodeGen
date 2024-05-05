import math

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def is_good_prime(p):
    for i in range(2, int(math.sqrt(p)) + 1):
        if p % i == 0:
            return False
    return True

def f(s, bad_primes):
    if s < 2:  # base case: single element or empty array
        return 0
    min_prime_divisor = None
    for p in range(2, s + 1):
        if s % p == 0 and is_good_prime(p) and p not in bad_primes:
            min_prime_divisor = p
            break
    if min_prime_divisor:
        return f(s // min_prime_divisor, bad_primes) + s
    else:  # no good prime divisor found
        return f(s // min_prime_divisor, bad_primes) - s

def solve(n, m, array, bad_primes):
    max_beauty = 0
    for i in range(len(array)):
        beauty = f(array[i], bad_primes)
        max_beauty = max(max_beauty, beauty)
    return max_beauty

# Read input from stdin
n, m = map(int, input().split())
array = list(map(int, input().split()))
bad_primes = list(map(int, input().split()))

# Calculate and print the maximum beauty
print(solve(n, m, array, bad_primes))
