import sys
from math import sqrt

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def min_prime_divisor(n):
    if n < 2:
        return None
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return i

def beauty(arr, bad_primes):
    total_beauty = 0
    for num in arr:
        if is_prime(num) and num not in bad_primes:
            total_beauty += min_prime_divisor(num)
        else:
            total_beauty -= min_prime_divisor(num)
    return total_beauty

def main():
    n, m = map(int, sys.stdin.readline().split())
    arr = list(map(int, sys.stdin.readline().split()))
    bad_primes = list(map(int, sys.stdin.readline().split()))

    print(beauty(arr, bad_primes))

if __name__ == "__main__":
    main()
