import sys
from math import gcd

def beauty_of_array(a, b):
    n = len(a)
    m = len(b)

    # First, sort the array in ascending order
    a.sort()

    max_beauty = 0

    for i in range(n):
        current_beauty = f(beauty_function(a[i]))
        if current_beauty > max_beauty:
            max_beauty = current_beauty

    return max_beauty

def beauty_function(x):
    p = min_prime_divisor(x)
    if is_good_prime(p):
        return x + f(beauty_function(x // p))
    else:
        return x - f(beauty_function(x // p))

def min_prime_divisor(x):
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0 and is_good_prime(i):
            return i
    return x

def is_good_prime(x):
    global bad_primes
    for p in bad_primes:
        if p > x:
            break
        if x % p == 0:
            return False
    return True

# Read input from stdin
n, m = map(int, sys.stdin.readline().split())
a = list(map(int, sys.stdin.readline().split()))
bad_primes = list(map(int, sys.stdin.readline().split()))

print(beauty_of_array(a, bad_primes))
