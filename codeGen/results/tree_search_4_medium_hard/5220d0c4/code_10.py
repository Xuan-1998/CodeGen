import sys
from math import sqrt, ceil

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(ceil(sqrt(n))) + 1):
        if n % i == 0:
            return False
    return True

def find_min_prime_divisor(n):
    for i in range(2, int(ceil(sqrt(n))) + 1):
        if n % i == 0 and is_prime(i):
            return i

def max_beauty(arr, bad_primes):
    n = len(arr)
    dp_table = [[-1] * (len(bad_primes) + 1) for _ in range(n + 1)]

    def dfs(left, right):
        if left > right:
            return 0
        if dp_table[left][right] != -1:
            return dp_table[left][right]
        
        beauty = 0
        min_prime_divisor = None
        
        for i in range(left, right + 1):
            prime_divisor = find_min_prime_divisor(arr[i])
            
            if prime_divisor not in bad_primes and (min_prime_divisor is None or prime_divisor < min_prime_divisor):
                min_prime_divisor = prime_divisor
            
        if min_prime_divisor:
            beauty += 1
        
        dp_table[left][right] = max(beauty, dfs(left + 1, right) if min_prime_divisor else 0)
        
        return dp_table[left][right]

    return dfs(0, n - 1)

# Read input from stdin
n, m = map(int, input().split())
arr = list(map(int, input().split()))
bad_primes = list(map(int, input().split()))

print(max_beauty(arr, bad_primes))
