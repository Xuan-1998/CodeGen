import sys

# Read input from stdin
n, m = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
bad_primes = set(map(int, sys.stdin.readline().split()))

# Initialize memoization dictionary
memo = {}

def beauty(i, j):
    if (i, j) in memo:
        return memo[(i, j)]
    
    max_beauty = 0
    for num in range(arr[i], arr[n] + 1):
        is_bad_prime = num in bad_primes
        min_prime_divisor = smallest_prime_divisor(num)
        
        if is_bad_prime:
            beauty_val = 0 if min_prime_divisor == num else -min_prime_divisor
        else:
            beauty_val = max_beauty if min_prime_divisor == num else min_prime_divisor
        
        max_beauty = max(max_beauty, beauty(i + 1, j) + beauty_val)
    
    memo[(i, j)] = max_beauty
    return max_beauty

def smallest_prime_divisor(n):
    for p in range(2, int(n**0.5) + 1):
        if n % p == 0:
            return p
    return n

print(beauty(0, m))
